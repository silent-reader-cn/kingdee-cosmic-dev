# 价目表控制单据物料范围配置-sm_pricelistctrlmatcfg

## 价目表控制单据物料范围配置-主表 t_sm_plctrlmatcfg

- **表名称：** 价目表控制单据物料范围配置-主表
- **表名：** t_sm_plctrlmatcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_plctrlmatcfg |  | fid |
| 2 | idx_sm_plctrlmatcfg_m0 |  | fmasterid |

---

## 单据配置单据体-子表 t_sm_plctrlmatcfgentry

- **表名称：** 单据配置单据体-子表
- **表名：** t_sm_plctrlmatcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenableparam | 启用参数判断 | bpchar | 1 |  | √ | '1' | 启用参数判断 |
| 3 | fmaterialkey | 物料字段标识 | varchar | 50 |  | √ | ' ' | 物料字段标识 |
| 4 | fpricelistkey | 价目表字段标识 | varchar | 50 |  | √ | ' ' | 价目表字段标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbillentity | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fparambelongapp | 参数所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_plctrlmatcfgentry_fk |  | fid |
| 2 | pk_sm_plctrlmatcfgentry |  | fentryid |

---

## 价目表控制单据物料范围配置-多语言表 t_sm_plctrlmatcfg_l

- **表名称：** 价目表控制单据物料范围配置-多语言表
- **表名：** t_sm_plctrlmatcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_plctrlmatcfg_l_0 |  | fid,flocaleid |
| 2 | pk_sm_plctrlmatcfg_l |  | fpkid |
