# 财产行为税申报主表-tcret_declare_main

## 财产行为税申报主表-主表 t_tcret_declare_main

- **表名称：** 财产行为税申报主表-主表
- **表名：** t_tcret_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fdetaildeclare | 明细申报 | varchar | 50 |  | √ | ' ' | 明细申报,枚举: true :是 false :否 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftransregional | 跨区域申报 | varchar | 50 |  | √ | ' ' | 跨区域申报,枚举: true :是 false :否 |
| 6 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fyjsehj | 已缴税额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已缴税额合计 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 10 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 缴款成功 payfailed :● 缴款失败 nopay :● 无需缴款 |
| 11 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftaxauthorityid | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdeclaredate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fsbrq | 申报时间 | timestamp | 0 |  |  | null | 申报时间 |
| 20 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 21 | fisxxwlqy | 小型微利企业 | varchar | 50 |  | √ | ' ' | 小型微利企业,枚举: true :是 false :否 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 24 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 25 | fjmsehj | 减免税额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额合计 |
| 26 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbqybtsehj | 应（补）退税额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 应（补）退税额合计 |
| 28 | fynsehj | 应纳税额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额合计 |
| 29 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |
| 32 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_declare_main |  | fid |
| 2 | idx_tcret_declare_main |  | forgid,ftaxauthorityid,fdeclaredate |

---

## 单据体-子表 t_tcret_declare_entry

- **表名称：** 单据体-子表
- **表名：** t_tcret_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsm | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 3 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: |
| 4 | ftaxstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 7 | fbqybtse | 应（补）退税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应（补）退税额 |
| 8 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 9 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 11 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已缴税额 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: yhsaq :印花税（按期） yhsac :印花税（按次） fcscj :房产税（从价） fcscz :房产税（从租） cztdsys :城镇土地使用税 hbsaq :环保税（按期） tdzzs :土地增值税（尾盘） tdzzsyj :土地增值税（预征） tdzzsqs :土地增值税（清算） |
| 14 | ftaxtypebrief | 税种简写 | varchar | 50 |  | √ | ' ' | 税种简写,枚举: yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 hbs :环保税 ccs :车船税 qs :契税 tdzzs :土地增值税 tdzzsyj :土地增值税 tdzzsqs :土地增值税 tdz :土地增值税 zys :资源税 szys :水资源税 tdzzszrjf :土地增值税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_declare_entry_fk |  | fid |
| 2 | pk_tcret_declare_entry |  | fentryid |
