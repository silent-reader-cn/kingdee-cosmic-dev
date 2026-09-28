# 预置数据版本信息-bd_predata_version

## 预置数据版本信息-主表 t_bd_preset_version

- **表名称：** 预置数据版本信息-主表
- **表名：** t_bd_preset_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fissendtoadmin | 是否发送通知到管理员 | bpchar | 1 |  | √ | '0' | 是否发送通知到管理员 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fisupdate | 是否更新 | bpchar | 1 |  | √ | '0' | 是否更新 |
| 6 | fversionnum | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 7 | fsource | 预置数据实体 | varchar | 36 |  | √ | ' ' | 预置数据实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_preset_version |  | fid |
| 2 | idx_bd_presetver_source |  | fsource |

---

## 预置数据版本信息-多语言表 t_bd_preset_version_l

- **表名称：** 预置数据版本信息-多语言表
- **表名：** t_bd_preset_version_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fguideinfo | 更新说明 | varchar | 1024 |  | √ | ' ' | 更新说明 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_preset_version_l |  | fpkid |
| 2 | idx_bd_presetver_l_id |  | fid,flocaleid |
