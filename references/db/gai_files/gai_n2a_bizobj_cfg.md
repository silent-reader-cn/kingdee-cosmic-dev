# 业务对象知识库-gai_n2a_bizobj_cfg

## 业务对象知识库-主表 t_gai_nl2api_bizobj_cfg

- **表名称：** 业务对象知识库-主表
- **表名：** t_gai_nl2api_bizobj_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frepodesc | 知识库描述 | varchar | 255 |  | √ | ' ' | 知识库描述 |
| 3 | fname | 知识库名称 | varchar | 100 |  | √ | ' ' | 知识库名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmetadata | 元数据 | varchar | 255 |  | √ | ' ' | 元数据 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fchunklengthlimit | 分块最大长度 | int4 | 32 |  | √ | 0 | 分块最大长度 |
| 9 | fentitynumber | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | frepo | 知识库版本 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 11 | findexmethod | 索引方式 | varchar | 50 |  | √ | ' ' | 索引方式,枚举: |
| 12 | fenablefielddesc | 字段描述向量化 | bpchar | 1 |  | √ | '1' | 字段描述向量化 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fmaxvaluecount | 值记录最大条数 | int4 | 32 |  | √ | 0 | 值记录最大条数 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ffielddesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 18 | fentitydesc | 业务对象描述 | varchar | 255 |  | √ | ' ' | 业务对象描述 |
| 19 | fenablesplitrepo | 拆分多知识库存储 | bpchar | 1 |  | √ | '1' | 拆分多知识库存储 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_n2a_bizobj_cfg_fname |  | fname |
| 2 | pk_t_gai_nl2api_bizobj_cfg |  | fid |

---

## 业务对象知识库-多语言表 t_gai_nl2api_bizobj_cfg_l

- **表名称：** 业务对象知识库-多语言表
- **表名：** t_gai_nl2api_bizobj_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 知识库名称 | varchar | 100 |  | √ | ' ' | 知识库名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_nl2api_bizobj_cfg_l |  | fpkid |
| 2 | idx_gai_n2a_bizobj_cfg_l_fid |  | fid |
