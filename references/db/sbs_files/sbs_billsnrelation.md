# 单据序列号关联表-sbs_billsnrelation

## 单据序列号关联表-主表 t_sbs_billsqnrelation

- **表名称：** 单据序列号关联表-主表
- **表名：** t_sbs_billsqnrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 来源分录id | int8 | 64 |  | √ | 0 | 来源分录id |
| 3 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 4 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fsrcisreq | 来源是否申请单据 | bpchar | 1 |  | √ | '0' | 来源是否申请单据 |
| 6 | fentrykey | 分录名称 | varchar | 100 |  | √ | ' ' | 分录名称 |
| 7 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 8 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 9 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |
| 10 | fsrcentrykey | 来源单据分录标识 | varchar | 50 |  | √ | ' ' | 来源单据分录标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_billsqnrelat_fbid |  | fbillid |
| 2 | idx_sbs_billsqnrelat_feidbt |  | fentryid,fbilltype |
| 3 | idx_sbs_billsqnrelat_fseid |  | fsrcentryid |
| 4 | t_sbs_billsqnrelation_pkey |  | fid |

---

## 序列号明细-子表 t_sbs_billsqnrelation_e

- **表名称：** 序列号明细-子表
- **表名：** t_sbs_billsqnrelation_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fimei | IMEI | varchar | 50 |  | √ | ' ' | IMEI |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmeid | MEID | varchar | 50 |  | √ | ' ' | MEID |
| 6 | fqualitystatus | 质量状态 | bpchar | 1 |  | √ | ' ' | 质量状态,枚举: A :合格 B :让步接收 C :待检 D :报废 E :损耗 F :待返工 |
| 7 | fbadhandmode | 检验处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 8 | fhandlestatus | 状态 | varchar | 50 |  | √ | 'A' | 状态,枚举: A :未处理 B :已处理 |
| 9 | finvorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsnmainfileid | 序列号主档id | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 11 | fsnnumber | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdamage | 途损 | bpchar | 1 |  | √ | '0' | 途损 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_billsqnrela_e_fid |  | fid |
| 2 | t_sbs_billsqnrelation_e_pkey |  | fentryid |
