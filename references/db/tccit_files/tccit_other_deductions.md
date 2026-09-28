# 其他税额减免优惠台账-tccit_other_deductions

## 其他税额减免优惠台账-主表 t_tccit_other_deductions

- **表名称：** 其他税额减免优惠台账-主表
- **表名：** t_tccit_other_deductions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_other_deductions |  | forgid,fyear |
| 2 | pk_tccit_other_deductions |  | fid |

---

## 单据体-子表 t_tccit_other_detentry

- **表名称：** 单据体-子表
- **表名：** t_tccit_other_detentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: qt :其他 dffxdbfjz :地方分享的部分减征 dffxdbfmz :地方分享的部分免征 |
| 3 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fproject | 优惠项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 6 | fdesc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 7 | fjmbl | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_other_detentry |  | fentryid |
| 2 | idx_tccit_other_detentry_fk |  | fid |
