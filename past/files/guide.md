# 写経ガイド — 4ステップで理解する order_manager.py

## テスト方法（全ステップ共通）

```bash
python stepX_xxx.py < test_input.txt
```

---

## テストデータの流れ（頭に入れてから読むこと）

```
商品3種, 発送可能数 M=2 (1日に各商品2個まで), D=3

① ORDER  AAAAAAAAAA → AAAAA x1  → 受理 (AAAAA: 1/2)
② ORDER  BBBBBBBBBB → AAAAA x2  → 拒否 (AAAAA: 1+2=3 > 2)
③ ORDER  CCCCCCCCCC → BBBBB x1  → 受理 (BBBBB: 1/2)
④ CANCEL AAAAAAAAAA              → 取消 (AAAAA: 1→0)
⑤ ORDER  DDDDDDDDDD → AAAAA x2  → 受理 (AAAAA: 0+2=2 ≤ 2) ← 取消のおかげ!
⑥ SHIP   01-02                   → CCCCCCCCCC, DDDDDDDDDD を発送
```

---

## Step 1 (0→1): 入力を正しく読めるか？

**集中すること**: パースだけ。業務ロジックなし。

ここで得るもの:
- `pos` 変数で「今どの行を読んでいるか」を管理するパターン
- ORDER は後続行の数が可変 (K行) なので、K を読んでからループする

Step 1 が動けば「入力の構造は正しく理解できた」と自信を持てる。

---

## Step 2 (1→10): 出力の形を作れるか？

**集中すること**: 正式フォーマットでの出力 + 注文の保存。

**前のステップからの差分**:
- `active_orders` 辞書を追加（状態②）
- ORDER → 常に受理して辞書に保存
- CANCEL → 辞書から削除
- SHIP → 発送日が一致する注文を探して、辞書順ソートで出力

**意図的にやらないこと**: 容量チェック。

Step 2 の出力は「全部受理」なので最終回答と違う。
だがこの段階で CANCEL と SHIP が正しく動いていることを確認できる。

---

## Step 3 (10→90): 業務ロジックを完成させる

**集中すること**: 発送枠の管理（状態①の追加）。

**前のステップからの差分（★マーク箇所）**:
- `shipment_counts` を追加（状態①）
- ORDER 内に容量チェックを追加
- ORDER 受理時に `+= qty`
- CANCEL 時に `-= qty`

```
Step 2 の ORDER:
    active_orders[order_id] = ...    ← 常に保存
    print(受理)                      ← 常に出力

Step 3 の ORDER:
    if can_accept:                   ← ★ 判定を追加
        shipment_counts[..] += qty   ← ★ 枠を予約
        active_orders[order_id] = ...
        print(受理)
    else:                            ← ★ 拒否を追加
        print(エラー)
```

**ここが最も重要なステップ**。Step 3 で正しい答えが出る。

---

## Step 4 (90→100): クラスに整理する

**集中すること**: コードの「置き場所」を整理するだけ。ロジック変更なし。

対応関係:

```
Step 3 の変数/コード         → Step 4 のクラス
─────────────────────────────────────────────
shipment_counts              → ShipmentTracker._counts
can_accept の for ループ      → ShipmentTracker.can_accept()
+= qty の for ループ         → ShipmentTracker.reserve()
-= qty の for ループ         → ShipmentTracker.release()

active_orders                → OrderManager._active_orders
ORDER ブロック               → OrderManager.process_order()
CANCEL ブロック              → OrderManager.process_cancel()
SHIP ブロック                → OrderManager.process_ship()

pos, lines, while ループ     → QueryParser
辞書 {"ship_date":..}        → Order dataclass
```

Step 3 のコードをコピペで移動しただけ。
新しいロジックは1行も書いていない。

---

## 写経の進め方

1. **Step 1 を写経** → 動かす → 入力が正しく読めることを確認
2. **Step 2 を写経** → 動かす → 出力のフォーマットを確認（答えは間違ってていい）
3. **Step 3 を写経** → 動かす → 正しい答えが出ることを確認 ← ここがゴール
4. **Step 4 を写経** → 動かす → 出力が Step 3 と同じことを確認
5. **order_manager.py と Step 4 を見比べる** → ほぼ同じ構造だと気づく
