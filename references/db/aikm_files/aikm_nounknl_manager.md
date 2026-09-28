# 名词知识库管理-aikm_nounknl_manager

## 名词知识库管理-主表 t_aikm_noun_manager

- **表名称：** 名词知识库管理-主表
- **表名：** t_aikm_noun_manager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkmgroupentityid | 知识库分组 | varchar | 50 |  | √ | ' ' | 知识库分组 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [名词知识库管理分组 aikm_noun_manager_group](../aikm_files/aikm_noun_manager_group.md) |
| 4 | fadminrole | 管理员角色 | varchar | 255 |  | √ | ' ' | 管理员角色 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fadminrole_tag | 管理员角色_详情 | text | 0 |  |  | null | 管理员角色_详情 |
| 7 | fauditrole_tag | 审核角色_详情 | text | 0 |  |  | null | 审核角色_详情 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fviewuser | 浏览人员 | varchar | 255 |  | √ | ' ' | 浏览人员 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 11 | faudituser | 审核人员 | varchar | 255 |  | √ | ' ' | 审核人员 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fassistantcount | 助手数量 | int8 | 64 |  | √ | 0 | 助手数量 |
| 14 | fviewrole_tag | 浏览角色_详情 | text | 0 |  |  | null | 浏览角色_详情 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | faudituser_tag | 审核人员_详情 | text | 0 |  |  | null | 审核人员_详情 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fviewrole | 浏览角色 | varchar | 255 |  | √ | ' ' | 浏览角色 |
| 21 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 22 | fnounentityid | 名词知识库 | varchar | 50 |  | √ | ' ' | 名词知识库 |
| 23 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fkmrepoid | 知识库 | int8 | 64 |  | √ | 0 | [知识库配置方案 aikm_repo_scheme](../aikm_files/aikm_repo_scheme.md) |
| 25 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fviewuser_tag | 浏览人员_详情 | text | 0 |  |  | null | 浏览人员_详情 |
| 28 | feditrole_tag | 编辑角色_详情 | text | 0 |  |  | null | 编辑角色_详情 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 30 | fauditrole | 审核角色 | varchar | 255 |  | √ | ' ' | 审核角色 |
| 31 | feditrole | 编辑角色 | varchar | 255 |  | √ | ' ' | 编辑角色 |
| 32 | fadminuser | 管理员人员 | varchar | 255 |  | √ | ' ' | 管理员人员 |
| 33 | fedituser | 编辑人员 | varchar | 255 |  | √ | ' ' | 编辑人员 |
| 34 | fknlcount | 知识数量 | int8 | 64 |  | √ | 0 | 知识数量 |
| 35 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 36 | fedituser_tag | 编辑人员_详情 | text | 0 |  |  | null | 编辑人员_详情 |
| 37 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fdesc | 知识库描述 | varchar | 100 |  | √ | ' ' | 知识库描述 |
| 40 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 41 | fadminuser_tag | 管理员人员_详情 | text | 0 |  |  | null | 管理员人员_详情 |
| 42 | fauthorizestatus | 授权状态 | varchar | 50 |  | √ | ' ' | 授权状态,枚举: 0 :公开 1 :未授权 2 :已授权 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aikm_noun_manager_createorg |  | fcreateorgid |
| 2 | idx_t_aikm_noun_manager |  | fnumber |
| 3 | idx_t_aikm_noun_manager_master |  | fmasterid |
| 4 | pk_aikm_noun_manager |  | fid |

---

## 名词知识库管理-多语言表 t_aikm_noun_manager_l

- **表名称：** 名词知识库管理-多语言表
- **表名：** t_aikm_noun_manager_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aikm_noun_manager_l |  | fid,flocaleid |
| 2 | pk_aikm_noun_manager_l |  | fpkid |

---

## 名词知识库管理-使用范围表 t_aikm_noun_manager_u

- **表名称：** 名词知识库管理-使用范围表
- **表名：** t_aikm_noun_manager_u

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
| 1 | idx_t_aikm_noun_manager_u_uo |  | fuseorgid |
| 2 | pk_t_aikm_noun_manager_u |  | fdataid,fuseorgid |
