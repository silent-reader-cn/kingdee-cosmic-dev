# 库存水位因子-invp_levelfactor

## 库存水位因子-多语言表 t_invp_levelfactor_l

- **表名称：** 库存水位因子-多语言表
- **表名：** t_invp_levelfactor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 因子名称 | varchar | 255 |  | √ | ' ' | 因子名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_levelfactor_l |  | fid,flocaleid |
| 2 | pk_invp_levelfactor_l |  | fpkid |

---

## 参数设置-子表 t_invp_levelfactorentry

- **表名称：** 参数设置-子表
- **表名：** t_invp_levelfactorentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelfieldkey | 关联字段（标识） | varchar | 255 |  | √ | ' ' | 关联字段（标识） |
| 3 | fislock | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 4 | frelentity | 关联实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fismustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fplantype | 计划类型 | bpchar | 1 |  | √ | 'A' | 计划类型,枚举: A :再订货点 B :最大最小 C :平衡利库 D :固定期间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frelfield | 关联字段 | varchar | 50 |  | √ | ' ' | 关联字段 |
| 10 | fisshow | 可见 | bpchar | 1 |  | √ | '0' | 可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_levelfactorentry |  | fentryid |
| 2 | idx_invp_levelfactorentry_fplantype_frelentity |  | fplantype,frelentity |
| 3 | idx_invp_levelfactorentry_fid |  | fid |

---

## 库存水位因子-主表 t_invp_levelfactor

- **表名称：** 库存水位因子-主表
- **表名：** t_invp_levelfactor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisfixedperiod | 固定期间 | bpchar | 1 |  | √ | '0' | 固定期间 |
| 3 | fname | 因子名称 | varchar | 50 |  | √ | ' ' | 因子名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisbalanceinv | 平衡利库 | bpchar | 1 |  | √ | '0' | 平衡利库 |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 因子类型 | bpchar | 1 |  | √ | 'A' | 因子类型,枚举: A :日期 B :数量 |
| 14 | fismaxandmin | 最大最小 | bpchar | 1 |  | √ | '0' | 最大最小 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 因子编码 | varchar | 30 |  | √ | ' ' | 因子编码 |
| 17 | fisreorderpoint | 再订货点 | bpchar | 1 |  | √ | '0' | 再订货点 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_levelfactor |  | fid |
| 2 | idx_invp_levelfactor_fnum |  | fnumber |
