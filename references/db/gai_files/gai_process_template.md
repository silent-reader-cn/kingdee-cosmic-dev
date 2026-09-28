# 任务流模板-gai_process_template

## 任务流模板-主表 t_gai_process_template

- **表名称：** 任务流模板-主表
- **表名：** t_gai_process_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 模板类别 | int8 | 64 |  | √ | 0 | [任务流模板分组 gai_process_tpl_group](../gai_files/gai_process_tpl_group.md) |
| 3 | fisupload | 支持上传附件 | bpchar | 1 |  | √ | '0' | 支持上传附件 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 预置 | varchar | 50 |  | √ | ' ' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | favatar | 模板头像 | varchar | 512 |  | √ | ' ' | 模板头像 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fmaxuploadnums | 最大文件数量 | int8 | 64 |  | √ | 10 | 最大文件数量 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fpublish | 发布为技能 | varchar | 50 |  | √ | ' ' | 发布为技能 |
| 17 | fflow | 流程编排 | text | 0 |  |  | null | 流程编排 |
| 18 | fisnew | isnew | bpchar | 1 |  | √ | '0' | isnew |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fprocess_group | 任务流分组 | int8 | 64 |  | √ | 0 | [GPT任务分组 gai_process_group](../gai_files/gai_process_group.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | ffiletypes | 文件类型 | varchar | 255 |  | √ | ' ' | 文件类型 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fblgids | 许可分组ID | varchar | 50 |  | √ | ' ' | 许可分组ID |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fdesc | 引导语 | varchar | 1000 |  | √ | ' ' | 引导语 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 31 | fservicedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_process_template_master |  | fmasterid |
| 2 | pk_gai_process_template |  | fid |
| 3 | idx_gai_process_template_name |  | fname |
| 4 | idx_t_gai_process_template_createorg |  | fcreateorgid |

---

## 应用-多选基础资料表 t_gai_process_app

- **表名称：** 应用-多选基础资料表
- **表名：** t_gai_process_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  |  | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_process_app |  | fpkid |
| 2 | idx_t_gai_process_app |  | fid,fbasedataid |

---

## 任务流模板-使用范围表 t_gai_process_template_u

- **表名称：** 任务流模板-使用范围表
- **表名：** t_gai_process_template_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_process_template_u |  | fdataid,fuseorgid |

---

## 任务流模板-多语言表 t_gai_process_template_l

- **表名称：** 任务流模板-多语言表
- **表名：** t_gai_process_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 引导语 | varchar | 150 |  | √ | ' ' | 引导语 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fservicedesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_process_template_l |  | fpkid |

---

## 推荐问法-子表 t_gai_suggestedask

- **表名称：** 推荐问法-子表
- **表名：** t_gai_suggestedask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffileids | 附件ID | varchar | 255 |  | √ | ' ' | 附件ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fquestion | 推荐问法 | varchar | 255 |  | √ | ' ' | 推荐问法 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_suggestedask |  | fentryid |
| 2 | idx_gai_suggestedask_fid |  | fid |
