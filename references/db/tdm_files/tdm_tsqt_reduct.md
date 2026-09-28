# 特殊群体减免优惠-tdm_tsqt_reduct

## 特殊群体减免优惠-主表 t_tdm_tsqt_reduct

- **表名称：** 特殊群体减免优惠-主表
- **表名：** t_tdm_tsqt_reduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjdlkpkrk | 建档立卡贫困人口 | numeric | 23 | 10 | √ | 0 | 建档立卡贫困人口 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ftsqttype | 特殊群体类型 | varchar | 50 |  | √ | ' ' | 特殊群体类型,枚举: zzjytysb :自主就业退役士兵 zdqt :重点群体 |
| 6 | fzzjytysb | 自主就业退役士兵 | numeric | 23 | 10 | √ | 0 | 自主就业退役士兵 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 采集月份.结束 | timestamp | 0 |  |  | null | 采集月份.结束 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fstartdate | 采集月份.开始 | timestamp | 0 |  |  | null | 采集月份.开始 |
| 14 | fdekcbzje | 定额扣除标准金额（人/年） | numeric | 23 | 10 | √ | 0 | 定额扣除标准金额（人/年） |
| 15 | fenable | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :禁用 1 :可用 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fdjsybnysry | 登记失业半年以上人员 | numeric | 23 | 10 | √ | 0 | 登记失业半年以上人员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_tsqt_reduct |  | fid |
| 2 | idx_t_tdm_tsqt_reduct |  | forgid,fstartdate,fenddate,ftsqttype |

---

## 单据体-子表 t_tdm_tsqt_reduct_entsum

- **表名称：** 单据体-子表
- **表名：** t_tdm_tsqt_reduct_entsum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbqcjjmed | 本期采集减免额度 | numeric | 23 | 10 | √ | 0 | 本期采集减免额度 |
| 3 | ftype | 特殊群体类型 | varchar | 50 |  | √ | ' ' | 特殊群体类型,枚举: 1 :自主就业退役士兵 2 :建档立卡贫困人口 3 :登记失业半年以上人员 |
| 4 | fcjrs | 采集人数 | int8 | 64 |  | √ | 0 | 采集人数 |
| 5 | fsywcjjmed | 剩余未采集减免额度 | numeric | 23 | 10 | √ | 0 | 剩余未采集减免额度 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tsqt_reduct_entsum_fk |  | fid |
| 2 | pk_tdm_tsqt_reduct_entsum |  | fentryid |

---

## 单据体-子表 t_tdm_tsqt_reduct_ent

- **表名称：** 单据体-子表
- **表名：** t_tdm_tsqt_reduct_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaffname | 员工姓名 | varchar | 255 |  | √ | ' ' | 员工姓名 |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbndkcjyfs | 本年度可采集月份数 | int8 | 64 |  | √ | 0 | 本年度可采集月份数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsykcjjmed | 剩余可采集减免额度 | numeric | 23 | 10 | √ | 0 | 剩余可采集减免额度 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fidnumber | 身份证号 | varchar | 20 |  | √ | ' ' | 身份证号 |
| 9 | fcertcode | 证件编号 | varchar | 50 |  | √ | ' ' | 证件编号 |
| 10 | fleavedate | 离职日期 | timestamp | 0 |  |  | null | 离职日期 |
| 11 | fspecialid | 特殊群体信息id | int8 | 64 |  | √ | 0 | 特殊群体信息id |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftype | 特殊群体类型 | varchar | 50 |  | √ | ' ' | 特殊群体类型,枚举: 0 :残疾人 1 :自主就业退役士兵 2 :建档立卡贫困人口 3 :登记失业半年以上人员 4 :毕业年度内高校毕业生 |
| 14 | fbqkcjjmed | 本期可采集减免额度 | numeric | 23 | 10 | √ | 0 | 本期可采集减免额度 |
| 15 | fssstartmonth | 缴纳社保起始月份 | timestamp | 0 |  |  | null | 缴纳社保起始月份 |
| 16 | fworkyear | 工作年度 | varchar | 50 |  | √ | ' ' | 工作年度 |
| 17 | fsjgzyfs | 实际工作月份数 | int8 | 64 |  | √ | 0 | 实际工作月份数 tdm_tsqt_reduct_sjgzyfs |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fycjjmed | 已采集减免额度 | numeric | 23 | 10 | √ | 0 | 已采集减免额度 |
| 20 | fbnkjmed | 本年可减免额度 | numeric | 23 | 10 | √ | 0 | 本年可减免额度 |
| 21 | fbndsykcjyfs | 本年度剩余可采集月份数 | int8 | 64 |  | √ | 0 | 本年度剩余可采集月份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tsqt_reduct_ent_fk |  | fid |
| 2 | pk_tdm_tsqt_reduct_ent |  | fentryid |
