# quo 模块表清单

> 本模块共收录 **37** 张表定义，来自 `quo_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope quo
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pur_bidbill` | 竞价单-主表 | 62 | [quo_bidbill.md](./quo_bidbill.md) |
| 2 | `t_pur_bidbill_a` | 竞价单-分表 | 32 | [quo_bidbill.md](./quo_bidbill.md) |
| 3 | `t_pur_bidbill_l` | 竞价单-多语言表 | 5 | [quo_bidbill.md](./quo_bidbill.md) |
| 4 | `t_pur_bidbillentry` | 商品分录-子表 | 34 | [quo_bidbill.md](./quo_bidbill.md) |
| 5 | `t_pur_bidbillentry_a` | 商品分录-分表 | 27 | [quo_bidbill.md](./quo_bidbill.md) |
| 6 | `t_pur_bidbillquote` | 报价分录-子表 | 19 | [quo_bidbill.md](./quo_bidbill.md) |
| 7 | `t_pur_bidbillsupplier` | 竞价情况分录-子表 | 18 | [quo_bidbill.md](./quo_bidbill.md) |
| 8 | `t_pur_bidbillsupplier_att` | 附件-附件表 | 3 | [quo_bidbill.md](./quo_bidbill.md) |
| 9 | `t_pur_compare` | 比价查询-主表 | 40 | [quo_compare.md](./quo_compare.md) |
| 10 | `t_pur_compare_a` | 比价查询-分表 | 14 | [quo_compare.md](./quo_compare.md) |
| 11 | `t_pur_compare_l` | 比价查询-多语言表 | 4 | [quo_compare.md](./quo_compare.md) |
| 12 | `t_pur_comparentry` | 比价单分录-子表 | 42 | [quo_compare.md](./quo_compare.md) |
| 13 | `t_pur_comparentry_a` | 比价单分录-分表 | 43 | [quo_compare.md](./quo_compare.md) |
| 14 | `t_pur_inquiry` | 我要报价-主表 | 55 | [quo_inquiry.md](./quo_inquiry.md) |
| 15 | `t_pur_inquiry_a` | 我要报价-分表 | 29 | [quo_inquiry.md](./quo_inquiry.md) |
| 16 | `t_pur_inquiry_l` | 我要报价-多语言表 | 4 | [quo_inquiry.md](./quo_inquiry.md) |
| 17 | `t_pur_inquiryentry` | 商品分录-子表 | 35 | [quo_inquiry.md](./quo_inquiry.md) |
| 18 | `t_pur_inquiryentry_a` | 商品分录-分表 | 24 | [quo_inquiry.md](./quo_inquiry.md) |
| 19 | `t_pur_inquirysupplier` | 报价分录-子表 | 12 | [quo_inquiry.md](./quo_inquiry.md) |
| 20 | `t_pur_inquiryturnslog` | 单据体-子表 | 9 | [quo_inquiry.md](./quo_inquiry.md) |
| 21 | `t_pur_message` | 消息查询-主表 | 15 | [quo_message.md](./quo_message.md) |
| 22 | `t_pur_message_l` | 消息查询-多语言表 | 5 | [quo_message.md](./quo_message.md) |
| 23 | `t_pur_notice` | 公告-主表 | 23 | [quo_notice.md](./quo_notice.md) |
| 24 | `t_pur_notice_a` | 公告-分表 | 17 | [quo_notice.md](./quo_notice.md) |
| 25 | `t_pur_notice_l` | 公告-多语言表 | 5 | [quo_notice.md](./quo_notice.md) |
| 26 | `t_pur_notice_reply` | 供应商答复分录-子表 | 7 | [quo_notice.md](./quo_notice.md) |
| 27 | `t_pur_notice_reply_fj` | 答复附件-附件表 | 3 | [quo_notice.md](./quo_notice.md) |
| 28 | `t_pur_noticesupplier` | 供应商分录-子表 | 9 | [quo_notice.md](./quo_notice.md) |
| 29 | `t_pur_quote` | 报价记录-主表 | 48 | [quo_quote.md](./quo_quote.md) |
| 30 | `t_pur_quote_a` | 报价记录-分表 | 16 | [quo_quote.md](./quo_quote.md) |
| 31 | `t_pur_quote_l` | 报价记录-多语言表 | 4 | [quo_quote.md](./quo_quote.md) |
| 32 | `t_pur_quote_lk` | 关联子实体-子表 | 6 | [quo_quote.md](./quo_quote.md) |
| 33 | `t_pur_quote_tc` | 报价记录-关联追踪表 | 7 | [quo_quote.md](./quo_quote.md) |
| 34 | `t_pur_quote_wb` | 报价记录-反写记录表 | 10 | [quo_quote.md](./quo_quote.md) |
| 35 | `t_pur_quotentry` | 报价单分录-子表 | 39 | [quo_quote.md](./quo_quote.md) |
| 36 | `t_pur_quotentry_a` | 报价单分录-分表 | 34 | [quo_quote.md](./quo_quote.md) |
| 37 | `t_pur_quotentry_lk` | 关联子实体-子表 | 8 | [quo_quote.md](./quo_quote.md) |
