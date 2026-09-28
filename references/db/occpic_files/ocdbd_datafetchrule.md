# 取数规则-ocdbd_datafetchrule

## 字段映射-分表 t_ocdbd_rule_colmap_f

- **表名称：** 字段映射-分表
- **表名：** t_ocdbd_rule_colmap_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldformuladesc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 3 | ffieldformula | 计算公式 | text | 0 |  |  | null | 计算公式 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fconverttype | 取值 | varchar | 10 |  | √ | ' ' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 3 :常量 |
| 6 | fconditionformula | 条件取值计算公式 | text | 0 |  |  | null | 条件取值计算公式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_rule_colmap_f_fid |  | fid |
| 2 | pk_ocdbd_rule_colmap_f |  | fentryid |

---

## 取数规则-主表 t_ocdbd_datafetchrule

- **表名称：** 取数规则-主表
- **表名：** t_ocdbd_datafetchrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffilterscheme | 自定义过滤条件 | text | 0 |  |  | null | 自定义过滤条件 |
| 6 | fdestbillentity | 目标数据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatetype | 取数方式 | bpchar | 1 |  | √ | ' ' | 取数方式,枚举: 1 :字段映射 2 :转换规则 |
| 13 | fconvertruleid | 来源数据转换规则 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fbillentity | 来源数据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 18 | fcomparefield | 关联单据最近修改时间比较字段 | varchar | 100 |  | √ | ' ' | 关联单据最近修改时间比较字段,枚举: |
| 19 | fdatatype | 业务取数规则 | bpchar | 1 |  | √ | ' ' | 业务取数规则,枚举: A :预算取数规则 B :返利取数规则 Z :运营取数规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_datafetchrule_no |  | fnumber |
| 2 | pk_ocdbd_datafetchrule |  | fid |

---

## 字段映射-子表 t_ocdbd_rule_colmap

- **表名称：** 字段映射-子表
- **表名：** t_ocdbd_rule_colmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffulldestcol | 目标字段全标识 | varchar | 100 |  | √ | ' ' | 目标字段全标识 |
| 3 | fdestcol | 目标字段标识 | varchar | 100 |  | √ | ' ' | 目标字段标识 |
| 4 | fissummary | 是否可汇总 | bpchar | 1 |  | √ | '0' | 是否可汇总 |
| 5 | fsumcol | 汇总至字段 | varchar | 100 |  | √ | ' ' | 汇总至字段,枚举: |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffullsrccol | 来源字段全标识 | varchar | 100 |  | √ | ' ' | 来源字段全标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsrccol | 来源字段标识 | varchar | 100 |  | √ | ' ' | 来源字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_rule_colmap_fid |  | fid |
| 2 | pk_ocdbd_rule_colmap |  | fentryid |

---

## 取数规则-多语言表 t_ocdbd_datafetchrule_l

- **表名称：** 取数规则-多语言表
- **表名：** t_ocdbd_datafetchrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_datafetchrule_l |  | fpkid |
| 2 | idx_ocdbd_datafetchrule_flid |  | fid,flocaleid |
