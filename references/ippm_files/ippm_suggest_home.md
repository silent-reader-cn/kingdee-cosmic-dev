# 反馈建议-ippm_suggest_home

## 反馈建议-主表 t_ippm_problemlist

- **表名称：** 反馈建议-主表
- **表名：** t_ippm_problemlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplication | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fcreate | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | faging | 账龄 | int4 | 32 |  | √ | 0 | 账龄 |
| 5 | fpriority | fpriority | varchar | 50 |  | √ | ' ' |  |
| 6 | ftenementid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 7 | fisdelete | 是否删除 | bpchar | 1 |  | √ | '0' | 是否删除 |
| 8 | ftenementname | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 9 | fissuedescription | 建议描述 | varchar | 255 |  | √ | ' ' | 建议描述 |
| 10 | faccount | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |
| 11 | fpcsnumber | PCS项目编号 | varchar | 50 |  | √ | ' ' | PCS项目编号 |
| 12 | fisgcp | 研发协助 | bpchar | 1 |  | √ | '0' | 研发协助 |
| 13 | ftitle | ftitle | varchar | 100 |  | √ | ' ' |  |
| 14 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: B :待答复 A :已答复 C :已解决 D :已撤销 E :处理中 |
| 15 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fissuedescription_tag | 建议描述_详情 | text | 0 |  |  | null | 建议描述_详情 |
| 17 | fchannel | 问题处理渠道 | varchar | 50 |  | √ | ' ' | 问题处理渠道 |
| 18 | fversion | 金蝶云.星空旗舰版版本号 | varchar | 50 |  | √ | ' ' | 金蝶云.星空旗舰版版本号 |
| 19 | fcreateuidname | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 20 | fprocessorname | 下一步处理人 | varchar | 50 |  | √ | ' ' | 下一步处理人 |
| 21 | fisforum | 社区协助 | bpchar | 1 |  | √ | '0' | 社区协助 |
| 22 | fapplicationname | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 23 | ftenementnumber | 租户编码 | varchar | 50 |  | √ | ' ' | 租户编码 |
| 24 | flistanswer | flistanswer | varchar | 2000 |  | √ | ' ' |  |
| 25 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 26 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

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
| 2 | fuserlog | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 6 | fuseranswer | 答复人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
