# 数据迁移任务配置-dtmg_validatorcfg

## 单据并行数量-子表 t_dtmg_objparallelentry

- **表名称：** 单据并行数量-子表
- **表名：** t_dtmg_objparallelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmigobj | 对象名称 | varchar | 255 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 3 | fobjenable | 启用 | varchar | 1 |  | √ | ' ' | 启用 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_objparallelentry |  | fentryid |
| 2 | idx_dtmg_parallel_entry_fid |  | fid |

---

## 数据迁移任务配置-多语言表 t_dtmg_validatorcfg_l

- **表名称：** 数据迁移任务配置-多语言表
- **表名：** t_dtmg_validatorcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_validatorcfg_l |  | fpkid |
| 2 | idx_dtmg_valid_fid |  | fid,flocaleid |

---

## 单据体-子表 t_dtmg_validatorcfgentry

- **表名称：** 单据体-子表
- **表名：** t_dtmg_validatorcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 启用 | varchar | 1 |  | √ | ' ' | 启用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fimplclass | 实现类 | varchar | 255 |  | √ | ' ' | 实现类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_validatorcfgentry |  | fentryid |
| 2 | idx_dtmg_valid_entry_fid |  | fid |

---

## 单据体-多语言表 t_dtmg_validatorcfgentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_dtmg_validatorcfgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_validatorcfgentry_l |  | fpkid |
| 2 | idx_valid_entry_fenid |  | fentryid |

---

## 数据迁移任务配置-主表 t_dtmg_validatorcfg

- **表名称：** 数据迁移任务配置-主表
- **表名：** t_dtmg_validatorcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmcmcheck | 物料组织公共信息的分配策略检测 | varchar | 1 |  | √ | '1' | 物料组织公共信息的分配策略检测 |
| 7 | ftabmigtype | 表对表迁移使用读写模式 | varchar | 2 |  | √ | ' ' | 表对表迁移使用读写模式 |
| 8 | fallowanotheroption | 允许迁移任务被其他用户操作 | varchar | 1 |  | √ | '0' | 允许迁移任务被其他用户操作 |
| 9 | fbetafun | 开启Beta功能验证 | varchar | 50 |  | √ | ' ' | 开启Beta功能验证,枚举: 1 :增量迁移 2 :迁移校对 3 :在途审批 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fshadowlimit | 旗舰对数单据上限 | int4 | 32 |  | √ | 100000 | 旗舰对数单据上限 |
| 12 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbackuptime | 备查开启时间 | timestamp | 0 |  |  | null | 备查开启时间 |
| 16 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fparallelnum | 并行数量 | int4 | 32 |  | √ | 0 | 并行数量 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fbreakmaxnum | 断点任务子任务最大数量 | int4 | 32 |  | √ | 0 | 断点任务子任务最大数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_validatorcfg |  | fid |
| 2 | idx_dtmg_valid_num |  | fnumber |
