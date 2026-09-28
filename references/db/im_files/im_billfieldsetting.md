# 库存单据字段设置-im_billfieldsetting

## 字段分录-子表 t_im_fieldsettingentry

- **表名称：** 字段分录-子表
- **表名：** t_im_fieldsettingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | ffield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryentityid | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 8 | fisinverse | 是否红单字段 | bpchar | 1 |  | √ | '0' | 是否红单字段 |
| 9 | ffullfield | 字段全标识 | varchar | 100 |  | √ | ' ' | 字段全标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_bset_e_ffid |  | ffullfield |
| 2 | idx_im_bset_e_fid |  | fid |
| 3 | t_im_fieldsettingentry_pkey |  | fentryid |

---

## 库存单据字段设置-主表 t_im_billfieldsetting

- **表名称：** 库存单据字段设置-主表
- **表名：** t_im_billfieldsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbill | 单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_billfieldsetting_pkey |  | fid |
| 2 | idx_im_bset_fb |  | fbill |

---

## 库存单据字段设置-多语言表 t_im_billfieldsetting_l

- **表名称：** 库存单据字段设置-多语言表
- **表名：** t_im_billfieldsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_billfieldsting_l_fidlc |  | fid,flocaleid |
| 2 | t_im_billfieldsetting_l_pkey |  | fpkid |
