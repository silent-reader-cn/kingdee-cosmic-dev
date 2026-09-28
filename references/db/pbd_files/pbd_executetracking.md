# 业务追踪图方案-pbd_executetracking

## 业务追踪图方案-主表 t_pbd_executetracking

- **表名称：** 业务追踪图方案-主表
- **表名：** t_pbd_executetracking

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 方案名称 | varchar | 512 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisentrydim | 是否分录匹配 | bpchar | 1 |  | √ | '0' | 是否分录匹配 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 10 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_executetracking |  | fid |
| 2 | idx_pbd_executetrack_fnumber |  | fnumber |

---

## 业务追踪图方案-多语言表 t_pbd_executetracking_l

- **表名称：** 业务追踪图方案-多语言表
- **表名：** t_pbd_executetracking_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_executetracking_l |  | fpkid |
| 2 | idx_pbd_executetracking_l |  | fid,flocaleid |

---

## 主单据配置分录-子表 t_pbd_trackingentry

- **表名称：** 主单据配置分录-子表
- **表名：** t_pbd_trackingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 4 | fsourceentityid | 主实体 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_trackingentry_fid |  | fid,fsourceentityid |
| 2 | pk_pbd_trackingentry |  | fentryid |

---

## 目标单据关系分录-子表 t_pbd_trackingdetail

- **表名称：** 目标单据关系分录-子表
- **表名：** t_pbd_trackingdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fdefinelinkid | 联查服务 | varchar | 36 |  | √ | ' ' | [联查关系定义 pbd_definelinkbill](../pbd_files/pbd_definelinkbill.md) |
| 3 | ftargetentityid | 目标实体 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 4 | fexecutelinkconfig | 联查配置 | text | 0 |  |  | null | 联查配置 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | varchar | 36 |  | √ | ' ' | id |
| 7 | fentryid | fentryid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_trackingdetail |  | fdetailid |
| 2 | idx_pbd_trackingdetail_fid |  | fid,fentryid |
