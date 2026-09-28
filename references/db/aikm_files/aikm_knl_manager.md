# 知识库管理-aikm_knl_manager

## 知识库管理-使用范围表 t_aikm_knl_manager_u

- **表名称：** 知识库管理-使用范围表
- **表名：** t_aikm_knl_manager_u

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
| 1 | idx_t_aikm_knl_manager_u_uo |  | fuseorgid |
| 2 | pk_t_aikm_knl_manager_u |  | fdataid,fuseorgid |

---

## 知识库管理-主表 t_aikm_knl_manager

- **表名称：** 知识库管理-主表
- **表名：** t_aikm_knl_manager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkmgroupentityid | 知识库分组 | varchar | 36 |  | √ | ' ' | 知识库分组 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [知识库分组 aikm_knl_manager_group](../aikm_files/aikm_knl_manager_group.md) |
| 4 | fadminrole | 管理员角色 | varchar | 255 |  | √ | ' ' | 管理员角色 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fadminrole_tag | 管理员角色_详情 | text | 0 |  |  | null | 管理员角色_详情 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditrole_tag | 审核角色_详情 | text | 0 |  |  | null | 审核角色_详情 |
| 9 | fviewuser | 浏览人员 | varchar | 255 |  | √ | ' ' | 浏览人员 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | faudituser | 审核人员 | varchar | 255 |  | √ | ' ' | 审核人员 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fviewrole_tag | 浏览角色_详情 | text | 0 |  |  | null | 浏览角色_详情 |
| 14 | fassistantcount | 助手数量 | int4 | 32 |  | √ | 0 | 助手数量 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | faudituser_tag | 审核人员_详情 | text | 0 |  |  | null | 审核人员_详情 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fviewrole | 浏览角色 | varchar | 255 |  | √ | ' ' | 浏览角色 |
| 21 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fkmrepoid | 知识库 | int8 | 64 |  | √ | 0 | [知识库配置方案 aikm_repo_scheme](../aikm_files/aikm_repo_scheme.md) |
| 24 | fname | 名称 | varchar | 54 |  | √ | ' ' | 名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fviewuser_tag | 浏览人员_详情 | text | 0 |  |  | null | 浏览人员_详情 |
| 27 | feditrole_tag | 编辑角色_详情 | text | 0 |  |  | null | 编辑角色_详情 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fauditrole | 审核角色 | varchar | 255 |  | √ | ' ' | 审核角色 |
| 30 | feditrole | 编辑角色 | varchar | 255 |  | √ | ' ' | 编辑角色 |
| 31 | fadminuser | 管理员人员 | varchar | 255 |  | √ | ' ' | 管理员人员 |
| 32 | fedituser | 编辑人员 | varchar | 255 |  | √ | ' ' | 编辑人员 |
| 33 | fknlcount | 知识数量 | int4 | 32 |  | √ | 0 | 知识数量 |
| 34 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 35 | fkmentityid | 文档知识库 | varchar | 36 |  | √ | ' ' | 文档知识库 |
| 36 | fedituser_tag | 编辑人员_详情 | text | 0 |  |  | null | 编辑人员_详情 |
| 37 | fkmqaentityid | QA知识库 | varchar | 36 |  | √ | ' ' | QA知识库 |
| 38 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 40 | fdesc | 知识库描述 | varchar | 100 |  | √ | ' ' | 知识库描述 |
| 41 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 42 | fadminuser_tag | 管理员人员_详情 | text | 0 |  |  | null | 管理员人员_详情 |
| 43 | fauthorizestatus | 授权状态 | varchar | 50 |  | √ | ' ' | 授权状态,枚举: 0 :公开 1 :未授权 2 :已授权 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aikm_knl_manager_createorg |  | fcreateorgid |
| 2 | pk_t_aikm_knl_manager |  | fid |
| 3 | idx_t_aikm_knl_manager_master |  | fmasterid |
| 4 | idx_t_aikm_knl_manager |  | fnumber |

---

## 知识库管理-多语言表 t_aikm_knl_manager_l

- **表名称：** 知识库管理-多语言表
- **表名：** t_aikm_knl_manager_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 54 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 14 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aikm_knl_manager_l |  | fpkid |
| 2 | idx_t_aikm_knl_manager_l |  | fid,flocaleid |
