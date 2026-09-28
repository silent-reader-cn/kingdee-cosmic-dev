# 样品状态变更记录-qcbd_sample_state

## 状态信息分录-子表 t_qcbd_state_record

- **表名称：** 状态信息分录-子表
- **表名：** t_qcbd_state_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | 操作 | varchar | 20 |  | √ | ' ' | 操作,枚举: XJYP :新建 XTJY :下推检验单 JYWC :检验完成 JLLY :记录留样观察 XTZD :系统自动 XHYP :销毁样品 SCLY :删除留样观察 |
| 3 | fbeforestate | 变更前状态 | varchar | 20 |  | √ | ' ' | 变更前状态,枚举: CSH :初始化 CDZ :存档 JYZ :检验中 DXH :待销毁 |
| 4 | fafterstate | 变更后状态 | varchar | 20 |  | √ | ' ' | 变更后状态,枚举: CDZ :存档 JYZ :检验中 DXH :待销毁 YXH :已销毁 |
| 5 | foperator | 操作员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_state_record |  | fentryid |
| 2 | idx_qcbd_staterec_fid |  | fid |

---

## 样品状态变更记录-主表 t_qcbd_sample_state

- **表名称：** 样品状态变更记录-主表
- **表名：** t_qcbd_sample_state

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fledgerid | 样品台账主键 | int8 | 64 |  | √ | 0 | 样品台账主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_sample_state |  | fid |
| 2 | idx_qcbd_state_fledgerid |  | fledgerid |
