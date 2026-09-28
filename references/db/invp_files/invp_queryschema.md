# 因子取数方案-invp_queryschema

## 因子取数方案-主表 t_invp_queryschema

- **表名称：** 因子取数方案-主表
- **表名：** t_invp_queryschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fleveldimension | 水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 msplan_plan_dimension |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fplantype | 计划类型 | bpchar | 1 |  | √ | 'A' | 计划类型,枚举: A :再订货点 B :最大最小 C :平衡利库 D :固定期间 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 20 | flevelfactor | 水位因子 | int8 | 64 |  | √ | 0 | 库存水位因子 invp_levelfactor |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryschema_org |  | fcreateorgid |
| 2 | idx_t_invp_queryschema_master |  | fmasterid |
| 3 | pk_invp_queryschema |  | fid |
| 4 | idx_t_invp_queryschema_createorg |  | fcreateorgid |
| 5 | idx_invp_queryschema_fnum |  | fnumber |

---

## 因子取数方案-多语言表 t_invp_queryschema_l

- **表名称：** 因子取数方案-多语言表
- **表名：** t_invp_queryschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryschema_l |  | fid,flocaleid |
| 2 | pk_invp_queryschema_l |  | fpkid |

---

## 因子取数方案-使用范围表 t_invp_queryschema_u

- **表名称：** 因子取数方案-使用范围表
- **表名：** t_invp_queryschema_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_queryschema_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_queryschema_u_uo |  | fuseorgid |

---

## 取数规则配置-子表 t_invp_queryschemaentry

- **表名称：** 取数规则配置-子表
- **表名：** t_invp_queryschemaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqueryrule | 取数规则 | int8 | 64 |  | √ | 0 | 因子取数规则 invp_queryrule |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnextstep | 取不到值的处理方式 | bpchar | 1 |  | √ | 'A' | 取不到值的处理方式,枚举: A :读取下1条规则 B :标记例外信息 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryschemaentry_fid |  | fid |
| 2 | pk_invp_queryschemaentry |  | fentryid |
