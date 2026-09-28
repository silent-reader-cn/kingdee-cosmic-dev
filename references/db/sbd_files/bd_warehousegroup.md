# 仓库分组-bd_warehousegroup

## 仓库分组-多语言表 t_bd_warehousegroup_l

- **表名称：** 仓库分组-多语言表
- **表名：** t_bd_warehousegroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  |  | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_warehousegroup_l_pkey |  | fpkid |
| 2 | idx_bd_warehousegroup_l_fid |  | fid,flocaleid |

---

## 仓库分组-主表 t_bd_warehousegroup

- **表名称：** 仓库分组-主表
- **表名：** t_bd_warehousegroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fparentid | 上级分组 | int8 | 64 |  | √ | 0 | 仓库分组 bd_warehousegroup |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 8 | flongnumber | 长编码 | varchar | 255 |  |  | ' ' | 长编码 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_warehousegroup_number |  | fnumber |
| 2 | t_bd_warehousegroup_pkey |  | fid |
