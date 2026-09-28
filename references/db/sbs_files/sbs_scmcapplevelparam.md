# 供应链应用级参数-sbs_scmcapplevelparam

## 供应链应用级参数-多语言表 t_sbs_scmcapplevelparam_l

- **表名称：** 供应链应用级参数-多语言表
- **表名：** t_sbs_scmcapplevelparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 参数描述 | varchar | 1024 |  | √ | ' ' | 参数描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scmcapplevelparam_l_id |  | fid,flocaleid |
| 2 | pk_t_sbs_scmcapplevelparam_l |  | fpkid |

---

## 供应链应用级参数-主表 t_sbs_scmcapplevelparam

- **表名称：** 供应链应用级参数-主表
- **表名：** t_sbs_scmcapplevelparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 8 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | fdescription | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scmcapplevelparam_fnumber |  | fnumber |
| 2 | pk_t_sbs_scmcapplevelparam |  | fid |
