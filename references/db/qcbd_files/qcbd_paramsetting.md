# 质量公共参数设置-qcbd_paramsetting

## 质量公共参数设置-多语言表 t_qcbd_paramsetting_l

- **表名称：** 质量公共参数设置-多语言表
- **表名：** t_qcbd_paramsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 参数名称 | varchar | 150 |  | √ | ' ' | 参数名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_paramsetting_l |  | fpkid |
| 2 | idx_qcbd_pset_l_flocaleid |  | fid,flocaleid |

---

## 质量公共参数设置-主表 t_qcbd_paramsetting

- **表名称：** 质量公共参数设置-主表
- **表名：** t_qcbd_paramsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名称 | varchar | 150 |  | √ | ' ' | 参数名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 10 | fparamval | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 11 | fparamkey | 参数键 | varchar | 50 |  | √ | ' ' | 参数键 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_paramsetting |  | fparamkey |
| 2 | pk_qcbd_paramsetting |  | fid |
