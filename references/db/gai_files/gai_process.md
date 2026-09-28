# 任务流-gai_process

## 任务流-使用范围表 t_gai_process_u

- **表名称：** 任务流-使用范围表
- **表名：** t_gai_process_u

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
| 1 | pk_t_gai_process_u |  | fdataid,fuseorgid |
| 2 | idx_t_gai_process_u_uo |  | fuseorgid |

---

## 任务流-多语言表 t_gai_process_l

- **表名称：** 任务流-多语言表
- **表名：** t_gai_process_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | finputtips | 输入框提示语 | varchar | 150 |  | √ | ' ' | 输入框提示语 |
| 4 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 5 | fdesc | 引导语 | varchar | 150 |  | √ | ' ' | 引导语 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fservicedesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_process_l |  | fid |
| 2 | pk_t_gai_process_l |  | fpkid |

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

## 推荐问法-多语言表 t_gai_suggestedask_l

- **表名称：** 推荐问法-多语言表
- **表名：** t_gai_suggestedask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fquestion | 推荐问题 | varchar | 255 |  | √ | ' ' | 推荐问题 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_suggestedask_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_gai_suggestedask_l |  | fpkid |

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
| 4 | fquestion | 推荐问题 | varchar | 255 |  | √ | ' ' | 推荐问题 |
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

---

## 任务流-主表 t_gai_process

- **表名称：** 任务流-主表
- **表名：** t_gai_process

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [GPT任务分组 gai_process_group](../gai_files/gai_process_group.md) |
| 3 | fisupload | 支持上传附件 | bpchar | 1 |  | √ | '1' | 支持上传附件 |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 预置 | varchar | 1 |  |  | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | finputtips | 输入框提示语 | varchar | 50 |  | √ | ' ' | 输入框提示语 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fmaxuploadnums | 最大文件数量 | int8 | 64 |  | √ | 10 | 最大文件数量 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fflow | 流程编排 | text | 0 |  |  | null | 流程编排 |
| 17 | fpublish | 发布为技能 | varchar | 1 |  |  | '0' | 发布为技能 |
| 18 | fisnew | isnew | bpchar | 1 |  | √ | '0' | isnew |
| 19 | frecommend_question_num | frecommend_question_num | int8 | 64 |  | √ | 3 |  |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | frecommend_question_enable | frecommend_question_enable | bpchar | 1 |  | √ | '0' |  |
| 25 | fquestion_generate_way | fquestion_generate_way | varchar | 50 |  | √ | 'llm' |  |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  |  | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |
| 28 | ffiletypes | 文件类型 | varchar | 255 |  |  | ' ' | 文件类型 |
| 29 | flarge_model | flarge_model | varchar | 255 |  | √ | ' ' |  |
| 30 | frecommend_question_promp | frecommend_question_promp | varchar | 1000 |  | √ | ' ' |  |
| 31 | frecommend_question_promp_tag | frecommend_question_promp_tag | text | 0 |  |  | ' ' |  |
| 32 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fblgids | 许可分组ID | varchar | 512 |  | √ | '606' | 许可分组ID |
| 34 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |
| 35 | fdesc | 引导语 | varchar | 50 |  |  | ' ' | 引导语 |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 37 | fservicedesc | 描述 | varchar | 255 |  |  | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_process |  | fid |
| 2 | idx_t_gai_process |  | fpublish,fnumber |
| 3 | idx_t_gai_process_master |  | fmasterid |
| 4 | idx_t_gai_process_createorg |  | fcreateorgid |
