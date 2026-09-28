# 预缴申报查询-tcvat_prepay_declare_bill

## 单据体-子表 t_tctb_declare_entry

- **表名称：** 单据体-子表
- **表名：** t_tctb_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fszysno | fszysno | varchar | 50 |  | √ | ' ' |  |
| 3 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 4 | fyjsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 7 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 8 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 9 | fjmse | fjmse | numeric | 23 | 10 | √ | 0 |  |
| 10 | fynse | fynse | numeric | 23 | 10 | √ | 0 |  |
| 11 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: 1 :增值税 3 :城市维护建设税 4 :教育费附加 5 :地方教育附加 |
| 14 | fbqdybtse | 预缴金额 | numeric | 23 | 10 | √ | 0 | 预缴金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_entry |  | fentryid |
| 2 | idx_tctb_declare_entry_fk |  | fid |

---

## 预缴申报查询-主表 t_tcvat_prepay_declare

- **表名称：** 预缴申报查询-主表
- **表名：** t_tcvat_prepay_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbqybtse | 合计预缴金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计预缴金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: undeclare :● 未编制 editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 importing :● 已申报未导入 declared :● 申报成功 declarefailed :● 申报失败 |
| 9 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: 0 :● 未缴款 submitted :● 已提交待缴款 1 :● 已缴款 yypaid :● 预约成功 yypayfailed :● 预约失败 |
| 10 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 13 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftemplateid | 申报表模板主键 | int8 | 64 |  | √ | 0 | 申报表模板主键 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 22 | fsssbbid | 所属申报表id | varchar | 50 |  | √ | '0' | 所属申报表id |
| 23 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 24 | fdeductionperiod | 抵减税期 | varchar | 50 |  | √ | ' ' | 抵减税期,枚举: 0 :未抵减 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 25 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdeclareserialno | 申报编号 | varchar | 50 |  | √ | ' ' | 申报编号 |
| 27 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 28 | fprepayproject | 预缴项目 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_prepay_declare |  | forgid,fskssqq,fskssqz |
| 2 | pk_tcvat_prepay_declare |  | fid |
| 3 | idx_tcvat_prepay_declare_1 |  | fewblxh,fsbbid |
