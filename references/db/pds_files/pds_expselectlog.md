# 专家抽取日志-pds_expselectlog

## 专家抽取日志-主表 t_pds_expselectlog

- **表名称：** 专家抽取日志-主表
- **表名：** t_pds_expselectlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 抽取时间 | timestamp | 0 |  |  | null | 抽取时间 |
| 6 | fdescription | 抽取条件 | varchar | 2000 |  | √ | ' ' | 抽取条件 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 10 | fcreatorid | 抽取人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 pds_packagef7 |
| 12 | fturns | 抽取轮次 | int4 | 32 |  | √ | 0 | 抽取轮次 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_expselectlog_pid |  | fprojectid |
| 2 | pk_pds_expselectlog |  | fid |

---

## 单据体-子表 t_pds_expselectlogentry

- **表名称：** 单据体-子表
- **表名：** t_pds_expselectlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | fisinvite | 是否参加 | bpchar | 1 |  | √ | '0' | 是否参加 |
| 4 | fturns | 抽取轮次 | int4 | 32 |  | √ | 0 | 抽取轮次 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_expselectlogentry_fid |  | fid |
| 2 | pk_pds_expselectlogentry |  | fentryid |
