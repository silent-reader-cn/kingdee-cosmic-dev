# 申报底稿查询-tcvat_query_ybnsr

## 单据体-子表 t_tcvat_dg_ybnsr

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_ybnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 7 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 8 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 9 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 10 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 11 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 12 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 13 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 14 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 16 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 17 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 18 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 19 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_1 |  | fewblxh,fsbbid |
| 3 | idx_tcvat_dg_ybnsr |  | fid |

---

## 单据体-子表 t_tcvat_dg_xgmnsr

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_xgmnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 3 | fbhsxse | 应征增值税不含税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 应征增值税不含税销售额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 6 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 7 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 8 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 9 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 10 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 11 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 12 | fmsxse | 免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额 |
| 13 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 14 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_dg_xgmnsr |  | fid |
| 2 | pk_tcvat_dg_xgmnsr |  | fentryid |
| 3 | idx_tcvat_dg_xgmnsr_1 |  | fewblxh,fsbbid |

---

## 申报底稿查询-主表 t_tctb_draft_main

- **表名称：** 申报底稿查询-主表
- **表名：** t_tctb_draft_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faccrualplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 5 | ffetchstatus | ffetchstatus | varchar | 50 |  | √ | ' ' |  |
| 6 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型,枚举: draft_zzsybnsr :一般纳税人增值税 draft_zzsxgmnsr :小规模纳税人增值税 draft_zzsybnsr_ybhz :汇总一般企业增值税 draft_zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 draft_zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 |
| 7 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 10 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fjtnumber | fjtnumber | varchar | 50 |  | √ | ' ' |  |
| 13 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 14 | fflexbizdims | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fsbbno | fsbbno | varchar | 50 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 24 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 25 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 26 | fdataversion | fdataversion | varchar | 50 |  | √ | ' ' |  |
| 27 | ftype | ftype | varchar | 36 |  | √ | ' ' |  |
| 28 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 29 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 30 | fdeadline | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 31 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_draft_main |  | forgid,ftemplatetype,fstartdate,fenddate,fbillno |
| 2 | pk_tctb_draft_main |  | fid |

---

## 单据体-子表 t_tcvat_dg_ybnsr_ybhz

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_ybnsr_ybhz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 7 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 8 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 9 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 10 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 11 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 12 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 13 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 14 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 16 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 17 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 18 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 19 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr_ybhz |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_ybhz |  | fsbbid |
| 3 | idx_tcvat_dg_ybnsr_ybhz_1 |  | fewblxh,fsbbid |
