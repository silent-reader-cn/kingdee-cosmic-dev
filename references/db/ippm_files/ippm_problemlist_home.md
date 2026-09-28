# 反馈问题-ippm_problemlist_home

## 反馈问题-主表 t_ippm_problemlist

- **表名称：** 反馈问题-主表
- **表名：** t_ippm_problemlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fteststage | fteststage | varchar | 50 |  | √ | ' ' |  |
| 3 | fextend20 | fextend20 | varchar | 255 |  | √ | ' ' |  |
| 4 | ftenementid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 5 | fissuedescription | 问题描述 | varchar | 255 |  | √ | ' ' | 问题描述 |
| 6 | faccount | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |
| 7 | fpcsnumber | PCS项目编号 | varchar | 50 |  | √ | ' ' | PCS项目编号 |
| 8 | fisgcp | 研发协助 | bpchar | 1 |  | √ | '0' | 研发协助 |
| 9 | ftitle | ftitle | varchar | 100 |  | √ | ' ' |  |
| 10 | fextend19 | fextend19 | varchar | 255 |  | √ | ' ' |  |
| 11 | fcausebyupgrade | 升级导致的问题 | varchar | 50 |  | √ | ' ' | 升级导致的问题 |
| 12 | fissuedescription_tag | 问题描述_详情 | text | 0 |  |  | null | 问题描述_详情 |
| 13 | fextend14 | fextend14 | varchar | 255 |  | √ | ' ' |  |
| 14 | fextend13 | fextend13 | varchar | 255 |  | √ | ' ' |  |
| 15 | fextend12 | fextend12 | varchar | 255 |  | √ | ' ' |  |
| 16 | fextend11 | fextend11 | varchar | 255 |  | √ | ' ' |  |
| 17 | fextend18 | fextend18 | varchar | 255 |  | √ | ' ' |  |
| 18 | fextend17 | fextend17 | varchar | 255 |  | √ | ' ' |  |
| 19 | fchannel | 问题处理渠道 | varchar | 50 |  | √ | ' ' | 问题处理渠道 |
| 20 | fversion | 金蝶云.星空旗舰版版本号 | varchar | 50 |  | √ | ' ' | 金蝶云.星空旗舰版版本号 |
| 21 | fcreateuidname | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 22 | fextend16 | fextend16 | varchar | 255 |  | √ | ' ' |  |
| 23 | fextend15 | fextend15 | varchar | 255 |  | √ | ' ' |  |
| 24 | fprocessorname | 下一步处理人 | varchar | 50 |  | √ | ' ' | 下一步处理人 |
| 25 | fisforum | 社区协助 | bpchar | 1 |  | √ | '0' | 社区协助 |
| 26 | fextend10 | fextend10 | varchar | 255 |  | √ | ' ' |  |
| 27 | ftenementnumber | 租户编码 | varchar | 50 |  | √ | ' ' | 租户编码 |
| 28 | flistanswer | flistanswer | varchar | 2000 |  | √ | ' ' |  |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fapplication | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 31 | fcreate | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | faging | 账龄 | int4 | 32 |  | √ | 0 | 账龄 |
| 33 | fenvironment | fenvironment | varchar | 50 |  | √ | ' ' |  |
| 34 | fpriority | fpriority | varchar | 50 |  | √ | ' ' |  |
| 35 | fisdelete | 是否删除 | bpchar | 1 |  | √ | '0' | 是否删除 |
| 36 | ftenementname | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 37 | fextend5 | fextend5 | varchar | 255 |  | √ | ' ' |  |
| 38 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: B :待答复 A :已答复 C :已解决 D :已撤销 E :处理中 |
| 39 | fextend4 | fextend4 | varchar | 255 |  | √ | ' ' |  |
| 40 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fextend7 | fextend7 | varchar | 255 |  | √ | ' ' |  |
| 42 | fextend6 | fextend6 | varchar | 255 |  | √ | ' ' |  |
| 43 | fextend1 | fextend1 | varchar | 255 |  | √ | ' ' |  |
| 44 | fextend3 | fextend3 | varchar | 255 |  | √ | ' ' |  |
| 45 | fextend2 | fextend2 | varchar | 255 |  | √ | ' ' |  |
| 46 | fextend9 | fextend9 | varchar | 255 |  | √ | ' ' |  |
| 47 | fextend8 | fextend8 | varchar | 255 |  | √ | ' ' |  |
| 48 | fapplicationname | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 49 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_problemlist_number |  | fnumber |
| 2 | pk_t_ippm_problemlist |  | fid |

---

## 单据体-子表 t_ippm_problemlist_log

- **表名称：** 单据体-子表
- **表名：** t_ippm_problemlist_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserlog | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flogdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foperation | 操作 | varchar | 80 |  | √ | ' ' | 操作 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_problemlist_log |  | fentryid |
| 2 | idx_ippm_problemlist_log_fid |  | fid |

---

## 单据体-子表 t_ippm_problemlist_entity

- **表名称：** 单据体-子表
- **表名：** t_ippm_problemlist_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fanswercontent | 答复内容 | varchar | 255 |  | √ | ' ' | 答复内容 |
| 3 | fanswerdate | 答复时间 | timestamp | 0 |  |  | null | 答复时间 |
| 4 | fanswercontent_tag | 答复内容_详情 | text | 0 |  |  | null | 答复内容_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fuseranswer | 答复人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisaccepted | 是否采纳 | varchar | 50 |  | √ | ' ' | 是否采纳 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 来源 | varchar | 80 |  | √ | ' ' | 来源,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_problemlist_entity_fid |  | fid |
| 2 | pk_t_ippm_problemlist_entity |  | fentryid |
