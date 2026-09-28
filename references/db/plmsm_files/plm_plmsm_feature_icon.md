# 业务模型特性总结-plm_plmsm_feature_icon

## 业务模型特性总结-主表 t_plmsm_feature_icon

- **表名称：** 业务模型特性总结-主表
- **表名：** t_plmsm_feature_icon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftips | 提示（废弃） | varchar | 255 |  | √ | ' ' | 提示（废弃） |
| 6 | fserialnumber | 图标排列顺序号 | int4 | 32 |  | √ | 0 | 图标排列顺序号 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ficon | 图标 | varchar | 500 |  | √ | ' ' | 图标 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fvisable | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见,枚举: 1 :可见 0 :不可见 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_feature_icon |  | fid |
| 2 | idx_plmsm_fe_icon_fnumber |  | fnumber |

---

## 业务模型特性总结-多语言表 t_plmsm_feature_icon_l

- **表名称：** 业务模型特性总结-多语言表
- **表名：** t_plmsm_feature_icon_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_fea_icon_l_fid |  | fid |
| 2 | pk_t_plmsm_feature_icon_l |  | fpkid |
