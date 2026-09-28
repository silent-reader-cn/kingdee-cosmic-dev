# 控件方案-ide_controlschema

## 控件方案-主表 t_meta_ctlschema

- **表名称：** 控件方案-主表
- **表名：** t_meta_ctlschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 3 | fpreviewimg | 预览图 | varchar | 255 |  |  | null | 预览图 |
| 4 | fschemaid | 方案 id | varchar | 50 |  | √ | ' ' | 方案 id |
| 5 | fisvid | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 6 | fmoduleid | 领域标识 | varchar | 50 |  | √ | ' ' | 领域标识 |
| 7 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_ctlschema_pkey |  | fid |
| 2 | idx_t_meta_ctlschema_schemaid |  | fschemaid |

---

## 控件方案-多语言表 t_meta_ctlschema_l

- **表名称：** 控件方案-多语言表
- **表名：** t_meta_ctlschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 3 | fschemaname | 方案名称 | varchar | 200 |  | √ | ' ' | 方案名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_ctlschema_l_pkey |  | fpkid |
| 2 | idx_t_meta_ctlschema_l |  | fid,flocaleid |
