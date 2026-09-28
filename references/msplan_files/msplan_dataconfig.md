# 字段设置-msplan_dataconfig

## 字段设置-多语言表 t_msplan_dataconfig_l

- **表名称：** 字段设置-多语言表
- **表名：** t_msplan_dataconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dataconfig_l |  | fpkid |
| 2 | idx_msplan_dataconfig_l |  | fid,flocaleid |

---

## 单据体-子表 t_msplan_dataconfigentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_dataconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvnew | 新增可见 | bpchar | 1 |  | √ | '0' | 新增可见 |
| 3 | fsysmustinput | 系统预设必录 | bpchar | 1 |  | √ | '0' | 系统预设必录 |
| 4 | fsubmitenabled | 提交锁定 | bpchar | 1 |  | √ | '0' | 提交锁定 |
| 5 | fvedit | 编辑可见 | bpchar | 1 |  | √ | '0' | 编辑可见 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fallfieldkey | 字段标识(全) | varchar | 100 |  | √ | ' ' | 字段标识(全) |
| 8 | feditenabled | 修改锁定 | bpchar | 1 |  | √ | '0' | 修改锁定 |
| 9 | fvaudit | 审核可见 | bpchar | 1 |  | √ | '0' | 审核可见 |
| 10 | fisdatabase | 是否数据库字段 | bpchar | 1 |  | √ | '0' | 是否数据库字段 |
| 11 | fauditenabled | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 12 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 13 | fvview | 查看可见 | bpchar | 1 |  | √ | '0' | 查看可见 |
| 14 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 15 | fdefaultfuncparam | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 16 | fvsubmit | 提交可见 | bpchar | 1 |  | √ | '0' | 提交可见 |
| 17 | fenabled | 新增锁定 | bpchar | 1 |  | √ | '0' | 新增锁定 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fvinit | 初始可见 | bpchar | 1 |  | √ | '0' | 初始可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dataconfigentry |  | fentryid |
| 2 | idx_msplan_dataconfigentry |  | fid,fseq |

---

## 字段设置-主表 t_msplan_dataconfig

- **表名称：** 字段设置-主表
- **表名：** t_msplan_dataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillformid | 元数据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flayoutsolution | 单据布局方案 | varchar | 50 |  | √ | ' ' | 单据布局方案,枚举: |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_dataconfig |  | fnumber |
| 2 | pk_t_msplan_dataconfig |  | fid |

---

## 单据体-多语言表 t_msplan_dataconfigentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_msplan_dataconfigentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 2 | ffieldname | 字段名称 | varchar | 1000 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_dcentry_l |  | fpkid |
| 2 | idx_msplan_dcentry_l |  | fentryid,flocaleid |
