# sou 模块表清单

> 本模块共收录 **68** 张表定义，来自 `sou_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category sou
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pur_bidbill` | 竞价发布-主表 | 62 | [sou_bidbill.md](./sou_bidbill.md) |
| 2 | `t_pur_bidbill` | 竞价定标-主表 | 62 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 3 | `t_pur_bidbill_a` | 竞价发布-分表 | 32 | [sou_bidbill.md](./sou_bidbill.md) |
| 4 | `t_pur_bidbill_a` | 竞价定标-分表 | 32 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 5 | `t_pur_bidbill_l` | 竞价发布-多语言表 | 5 | [sou_bidbill.md](./sou_bidbill.md) |
| 6 | `t_pur_bidbill_l` | 竞价定标-多语言表 | 5 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 7 | `t_pur_bidbill_lk` | 关联子实体-子表 | 6 | [sou_bidbill.md](./sou_bidbill.md) |
| 8 | `t_pur_bidbill_tc` | 竞价发布-关联追踪表 | 7 | [sou_bidbill.md](./sou_bidbill.md) |
| 9 | `t_pur_bidbill_tc` | 竞价定标-关联追踪表 | 7 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 10 | `t_pur_bidbill_wb` | 竞价发布-反写记录表 | 10 | [sou_bidbill.md](./sou_bidbill.md) |
| 11 | `t_pur_bidbill_wb` | 竞价定标-反写记录表 | 10 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 12 | `t_pur_bidbillentry` | 物料明细-子表 | 34 | [sou_bidbill.md](./sou_bidbill.md) |
| 13 | `t_pur_bidbillentry` | 竞价单分录-子表 | 34 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 14 | `t_pur_bidbillentry_a` | 物料明细-分表 | 27 | [sou_bidbill.md](./sou_bidbill.md) |
| 15 | `t_pur_bidbillentry_a` | 竞价单分录-分表 | 27 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 16 | `t_pur_bidbillentry_lk` | 关联子实体-子表 | 6 | [sou_bidbill.md](./sou_bidbill.md) |
| 17 | `t_pur_bidbillquote` | 报价分录-子表 | 19 | [sou_bidbill.md](./sou_bidbill.md) |
| 18 | `t_pur_bidbillquote` | 报价分录-子表 | 19 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 19 | `t_pur_bidbillsupplier` | 供应商分录-子表 | 18 | [sou_bidbill.md](./sou_bidbill.md) |
| 20 | `t_pur_bidbillsupplier` | 供应商分录-子表 | 18 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 21 | `t_pur_bidbillsupplier_att` | 附件-附件表 | 3 | [sou_bidbill.md](./sou_bidbill.md) |
| 22 | `t_pur_bidbillsupplier_att` | 附件-附件表 | 3 | [sou_bidbillcfm.md](./sou_bidbillcfm.md) |
| 23 | `t_pur_compare` | 定标单-主表 | 40 | [sou_compare.md](./sou_compare.md) |
| 24 | `t_pur_compare_a` | 定标单-分表 | 14 | [sou_compare.md](./sou_compare.md) |
| 25 | `t_pur_compare_l` | 定标单-多语言表 | 4 | [sou_compare.md](./sou_compare.md) |
| 26 | `t_pur_compare_lk` | 关联子实体-子表 | 6 | [sou_compare.md](./sou_compare.md) |
| 27 | `t_pur_compare_tc` | 定标单-关联追踪表 | 7 | [sou_compare.md](./sou_compare.md) |
| 28 | `t_pur_compare_wb` | 定标单-反写记录表 | 10 | [sou_compare.md](./sou_compare.md) |
| 29 | `t_pur_comparentry` | 报价详情信息-子表 | 42 | [sou_compare.md](./sou_compare.md) |
| 30 | `t_pur_comparentry_a` | 报价详情信息-分表 | 43 | [sou_compare.md](./sou_compare.md) |
| 31 | `t_pur_comparentry_lk` | 关联子实体-子表 | 8 | [sou_compare.md](./sou_compare.md) |
| 32 | `t_pur_comparquoentry` | 报价汇总分录-子表 | 14 | [sou_compare.md](./sou_compare.md) |
| 33 | `t_pur_inquiry` | 询价单-主表 | 55 | [sou_inquiry.md](./sou_inquiry.md) |
| 34 | `t_pur_inquiry_a` | 询价单-分表 | 29 | [sou_inquiry.md](./sou_inquiry.md) |
| 35 | `t_pur_inquiry_l` | 询价单-多语言表 | 4 | [sou_inquiry.md](./sou_inquiry.md) |
| 36 | `t_pur_inquiry_tc` | 询价单-关联追踪表 | 7 | [sou_inquiry.md](./sou_inquiry.md) |
| 37 | `t_pur_inquiry_wb` | 询价单-反写记录表 | 10 | [sou_inquiry.md](./sou_inquiry.md) |
| 38 | `t_pur_inquiryentry` | 物料分录-子表 | 35 | [sou_inquiry.md](./sou_inquiry.md) |
| 39 | `t_pur_inquiryentry` | 询价单物料列表-主表 | 35 | [sou_inquiryentryf7.md](./sou_inquiryentryf7.md) |
| 40 | `t_pur_inquiryentry_a` | 物料分录-分表 | 24 | [sou_inquiry.md](./sou_inquiry.md) |
| 41 | `t_pur_inquiryentry_lk` | 关联子实体-子表 | 8 | [sou_inquiry.md](./sou_inquiry.md) |
| 42 | `t_pur_inquiryn_lk` | 关联子实体-子表 | 6 | [sou_inquiry.md](./sou_inquiry.md) |
| 43 | `t_pur_inquirysupplier` | 供应商分录-子表 | 12 | [sou_inquiry.md](./sou_inquiry.md) |
| 44 | `t_pur_inquiryturns` | 报价范围分录-子表 | 6 | [sou_inquiry.md](./sou_inquiry.md) |
| 45 | `t_pur_inquiryturnslog` | 多轮报价面板分录-子表 | 9 | [sou_inquiry.md](./sou_inquiry.md) |
| 46 | `t_pur_message` | 消息管理-主表 | 15 | [sou_message.md](./sou_message.md) |
| 47 | `t_pur_message_l` | 消息管理-多语言表 | 5 | [sou_message.md](./sou_message.md) |
| 48 | `t_pur_notice` | 公告管理-主表 | 23 | [sou_notice.md](./sou_notice.md) |
| 49 | `t_pur_notice` | 公告-主表 | 23 | [sou_notice_query.md](./sou_notice_query.md) |
| 50 | `t_pur_notice_a` | 公告管理-分表 | 17 | [sou_notice.md](./sou_notice.md) |
| 51 | `t_pur_notice_l` | 公告管理-多语言表 | 5 | [sou_notice.md](./sou_notice.md) |
| 52 | `t_pur_notice_l` | 公告-多语言表 | 5 | [sou_notice_query.md](./sou_notice_query.md) |
| 53 | `t_pur_notice_lk` | 关联子实体-子表 | 6 | [sou_notice.md](./sou_notice.md) |
| 54 | `t_pur_notice_reply` | 供应商答复分录-子表 | 7 | [sou_notice.md](./sou_notice.md) |
| 55 | `t_pur_notice_reply_fj` | 答复附件-附件表 | 3 | [sou_notice.md](./sou_notice.md) |
| 56 | `t_pur_notice_tc` | 公告管理-关联追踪表 | 7 | [sou_notice.md](./sou_notice.md) |
| 57 | `t_pur_notice_wb` | 公告管理-反写记录表 | 10 | [sou_notice.md](./sou_notice.md) |
| 58 | `t_pur_noticesupplier` | 供应商分录-子表 | 9 | [sou_notice.md](./sou_notice.md) |
| 59 | `t_pur_noticesupplier_lk` | 关联子实体-子表 | 6 | [sou_notice.md](./sou_notice.md) |
| 60 | `t_pur_quote` | 报价单-主表 | 48 | [sou_quote.md](./sou_quote.md) |
| 61 | `t_pur_quote_a` | 报价单-分表 | 16 | [sou_quote.md](./sou_quote.md) |
| 62 | `t_pur_quote_l` | 报价单-多语言表 | 4 | [sou_quote.md](./sou_quote.md) |
| 63 | `t_pur_quote_tc` | 报价单-关联追踪表 | 7 | [sou_quote.md](./sou_quote.md) |
| 64 | `t_pur_quote_wb` | 报价单-反写记录表 | 10 | [sou_quote.md](./sou_quote.md) |
| 65 | `t_pur_quoten_lk` | 关联子实体-子表 | 6 | [sou_quote.md](./sou_quote.md) |
| 66 | `t_pur_quotentry` | 报价单分录-子表 | 39 | [sou_quote.md](./sou_quote.md) |
| 67 | `t_pur_quotentry_a` | 报价单分录-分表 | 34 | [sou_quote.md](./sou_quote.md) |
| 68 | `t_pur_quotentry_lk` | 关联子实体-子表 | 8 | [sou_quote.md](./sou_quote.md) |
