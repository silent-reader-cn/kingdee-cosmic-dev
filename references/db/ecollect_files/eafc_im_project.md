# 集成方案-eafc_im_project

## 集成方案-主表 tk_eafc_im_project

- **表名称：** 集成方案-主表
- **表名：** tk_eafc_im_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fgroupid | 方案分类 | int8 | 64 |  |  | null | [方案分类 eafc_im_proj_category](../ecollect_files/eafc_im_proj_category.md) |
| 3 | fk_eafc_execute_type | 启动类型 | varchar | 50 |  | √ | ' ' | 启动类型,枚举: 1 :定时启动 2 :人工启动 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_period_end | 归档期间.结束 | timestamp | 0 |  |  | null | 归档期间.结束 |
| 6 | fk_fpy_period_start | 归档开始期间 | int8 | 64 |  |  | null | [会计期间 fpy_period](../ebase_files/fpy_period.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 100 |  |  | null |  |
| 17 | fk_fpy_period_end | 归档结束期间 | int8 | 64 |  |  | null | [会计期间 fpy_period](../ebase_files/fpy_period.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fk_eafc_period | 归档期间 | varchar | 50 |  | √ | ' ' | 归档期间,枚举: 3 :本期 1 :上期 2 :上上期 |
| 20 | fk_eafc_lastexecutetime | 最近一次执行时间 | timestamp | 0 |  |  | null | 最近一次执行时间 |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fk_eafc_period_start | 归档期间.开始 | timestamp | 0 |  |  | null | 归档期间.开始 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fk_eafc_useorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 26 | fk_eafc_desc | 方案描述 | varchar | 500 |  | √ | ' ' | 方案描述 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_eafc_im_project_createorg |  | fcreateorgid |
| 2 | pk__eafc_im_project |  | fid |
| 3 | idx_tk_eafc_im_project_master |  | fmasterid |

---

## 集成方案-使用范围表 tk_eafc_im_project_u

- **表名称：** 集成方案-使用范围表
- **表名：** tk_eafc_im_project_u

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
| 1 | pk_tk_eafc_im_project_u |  | fdataid,fuseorgid |
| 2 | idx_tk_eafc_im_project_u_uo |  | fuseorgid |

---

## 集成方案-多语言表 tk_eafc_im_project_l

- **表名称：** 集成方案-多语言表
- **表名：** tk_eafc_im_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_im_project_l |  | fpkid |

---

## 内容单据体-子表 tk_eafc_im_proj_content

- **表名称：** 内容单据体-子表
- **表名：** tk_eafc_im_proj_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_content | 内容名称 | int8 | 64 |  |  | null | [集成内容 eafc_im_content](../ecollect_files/eafc_im_content.md) |
| 3 | fk_eafc_content_param | 内容参数 | varchar | 255 |  | √ | ' ' | 内容参数 |
| 4 | fk_eafc_content_param_tag | 内容参数_详情 | text | 0 |  |  | null | 内容参数_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_proj_content_fk |  | fid |
| 2 | pk__eafc_im_proj_content |  | fentryid |

---

## 组织单据体-子表 tk_eafc_im_proj_org

- **表名称：** 组织单据体-子表
- **表名：** tk_eafc_im_proj_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_org | 组织名称 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 6 | fk_eafc_arcorg | 组织名称 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_im_proj_org_fk |  | fid |
| 2 | pk__eafc_im_proj_org |  | fentryid |
