# 资产申请种类-fa_asset_apply_real

## 资产申请种类-主表 t_fa_assetapply_real

- **表名称：** 资产申请种类-主表
- **表名：** t_fa_assetapply_real

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fasset_picture | 物品图片 | varchar | 255 |  |  | ' ' | 物品图片 |
| 3 | fasset_name | fasset_name | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetapply_real_pkey |  | fid |

---

## 资产申请种类-多语言表 t_fa_assetapply_real_l

- **表名称：** 资产申请种类-多语言表
- **表名：** t_fa_assetapply_real_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fasset_name | 物品名称 | varchar | 100 |  | √ | ' ' | 物品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assetapply_real_l |  | fid,flocaleid |
| 2 | t_fa_assetapply_real_l_pkey |  | fpkid |
