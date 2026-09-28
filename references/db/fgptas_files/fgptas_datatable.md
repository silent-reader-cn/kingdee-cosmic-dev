# 数据表配置-fgptas_datatable

## 数据表字段-多语言表 t_fgptas_datatablefield_l

- **表名称：** 数据表字段-多语言表
- **表名：** t_fgptas_datatablefield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffielddesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 2 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
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
| 1 | idx_fgptas_datatablefield_l |  | fentryid,flocaleid |
| 2 | pk_fgptas_datatablefield_l |  | fpkid |

---

## 数据表字段-子表 t_fgptas_datatablefield

- **表名称：** 数据表字段-子表
- **表名：** t_fgptas_datatablefield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffcheckmeta | 元数据检查 | bpchar | 1 |  | √ | ' ' | 元数据检查,枚举: 0 :未生成元数据 1 :已生成元数据 2 :已提交删除 |
| 3 | ffixedvalue | 固定值 | varchar | 255 |  | √ | ' ' | 固定值 |
| 4 | ffieldpropertyjson | 字段属性Json | varchar | 255 |  | √ | ' ' | 字段属性Json |
| 5 | ffieldproperty | 字段属性 | varchar | 500 |  | √ | ' ' | 字段属性 |
| 6 | ffieldname | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffieldquery | 条件字段 | bpchar | 1 |  | √ | ' ' | 条件字段 |
| 9 | fispreset | 预置 | bpchar | 1 |  | √ | ' ' | 预置 |
| 10 | ffieldnumber | 字段编码 | varchar | 30 |  | √ | ' ' | 字段编码 |
| 11 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: Text :单行文本 Integer :整数 Decimal :小数 Basedata :基础资料 Assistant :辅助资料 Combo :下拉列表 Org :组织 Supplier :供应商 User :用户 Customer :客户 Currency :币别 Amount :金额 Materiel :物料 |
| 12 | ffieldpropertyjson_tag | 字段属性Json_详情 | text | 0 |  |  | null | 字段属性Json_详情 |
| 13 | ffielddesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_datatablefield_fid |  | fid |
| 2 | pk_fgptas_datatablefield |  | fentryid |

---

## 数据表配置-多语言表 t_fgptas_datatable_l

- **表名称：** 数据表配置-多语言表
- **表名：** t_fgptas_datatable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据表名称 | varchar | 50 |  | √ | ' ' | 数据表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 数据表补充描述 | varchar | 255 |  | √ | ' ' | 数据表补充描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_datatable_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_datatable_l |  | fpkid |

---

## 数据表配置-主表 t_fgptas_datatable

- **表名称：** 数据表配置-主表
- **表名：** t_fgptas_datatable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpcheckmeta | 元数据检查 | bpchar | 1 |  | √ | ' ' | 元数据检查,枚举: 0 :未生成元数据 1 :已生成元数据 2 :已提交删除 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpreset | 预置 | bpchar | 1 |  | √ | ' ' | 预置 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fretrievalplugin | 数据查询插件 | varchar | 150 |  | √ | ' ' | 数据查询插件 |
| 14 | fentityid | 元数据实体ID | varchar | 15 |  | √ | ' ' | 元数据实体ID |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 数据表名称 | varchar | 60 |  | √ | ' ' | 数据表名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcustomtable | 自定义表 | bpchar | 1 |  | √ | ' ' | 自定义表 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdescription | 数据表补充描述 | varchar | 255 |  | √ | ' ' | 数据表补充描述 |
| 21 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '7' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :接口 2 :实体表 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fgptas_datatable_createorg |  | fcreateorgid |
| 2 | idx_t_fgptas_datatable_master |  | fmasterid |
| 3 | pk_fgptas_datatable |  | fid |
| 4 | idx_fgptas_datatable_number |  | fnumber |

---

## 数据表配置-使用范围表 t_fgptas_datatable_u

- **表名称：** 数据表配置-使用范围表
- **表名：** t_fgptas_datatable_u

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
| 1 | pk_t_fgptas_datatable_u |  | fdataid,fuseorgid |
| 2 | idx_t_fgptas_datatable_u_uo |  | fuseorgid |
