# 智能录单映射模型-ocmem_aifieldmapmodel

## 字段分录-子表 t_ocmem_aifieldmapentry

- **表名称：** 字段分录-子表
- **表名：** t_ocmem_aifieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 3 | fqueryentitynumber | 查找实体标识 | varchar | 50 |  | √ | ' ' | 查找实体标识 |
| 4 | fmatchsymbol | 匹配方式 | varchar | 20 |  | √ | ' ' | 匹配方式,枚举: = :精确匹配 like :模糊匹配 |
| 5 | ffielddescription | 字段描述 | varchar | 200 |  | √ | ' ' | 字段描述 |
| 6 | ffieldname | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fqueryfieldname | 查找字段名 | varchar | 100 |  | √ | ' ' | 查找字段名 |
| 10 | fmustfill | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 11 | fqueryfieldnumber | 查找字段标识 | varchar | 100 |  | √ | ' ' | 查找字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_aifieldmapentry |  | fentryid |
| 2 | pk_ocmem_aifieldmape_fid |  | fid |

---

## 智能录单映射模型-主表 t_ocmem_aifieldmapmodel

- **表名称：** 智能录单映射模型-主表
- **表名：** t_ocmem_aifieldmapmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmapbillobj | 映射单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_aifieldmm_number |  | fnumber |
| 2 | pk_ocmem_aifieldmapmodel |  | fid |

---

## 智能录单映射模型-多语言表 t_ocmem_aifieldmapmodel_l

- **表名称：** 智能录单映射模型-多语言表
- **表名：** t_ocmem_aifieldmapmodel_l

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
| 1 | idx_ocmem_aifieldmm_l_flid |  | fid,flocaleid |
| 2 | pk_ocmem_aifieldmapmodel_l |  | fpkid |
