# 项目问题列表-ippm_problemlist

## 项目问题列表-主表 t_ippm_problemlist

- **表名称：** 项目问题列表-主表
- **表名：** t_ippm_problemlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fteststage | 测试阶段 | varchar | 50 |  | √ | ' ' | 测试阶段,枚举: unit :单元测试 function :功能测试 integration :集成测试 check :验收测试 else :其他 |
| 3 | fextend20 | 扩展字段20 | varchar | 255 |  | √ | ' ' | 扩展字段20 |
| 4 | ftenementid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 5 | fissuedescription | 问题描述 | varchar | 255 |  | √ | ' ' | 问题描述 |
| 6 | faccount | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |
| 7 | fpcsnumber | PCS项目编号 | varchar | 50 |  | √ | ' ' | PCS项目编号 |
| 8 | fisgcp | 研发协助 | bpchar | 1 |  | √ | '0' | 研发协助 |
| 9 | ftitle | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 10 | fextend19 | 扩展字段19 | varchar | 255 |  | √ | ' ' | 扩展字段19 |
| 11 | fcausebyupgrade | fcausebyupgrade | varchar | 50 |  | √ | ' ' |  |
| 12 | fissuedescription_tag | 问题描述_详情 | text | 0 |  |  | null | 问题描述_详情 |
| 13 | fextend14 | 扩展字段14 | varchar | 255 |  | √ | ' ' | 扩展字段14 |
| 14 | fextend13 | 扩展字段13 | varchar | 255 |  | √ | ' ' | 扩展字段13 |
| 15 | fextend12 | 扩展字段12 | varchar | 255 |  | √ | ' ' | 扩展字段12 |
| 16 | fextend11 | 扩展字段11 | varchar | 255 |  | √ | ' ' | 扩展字段11 |
| 17 | fextend18 | 扩展字段18 | varchar | 255 |  | √ | ' ' | 扩展字段18 |
| 18 | fextend17 | 扩展字段17 | varchar | 255 |  | √ | ' ' | 扩展字段17 |
| 19 | fchannel | 问题处理渠道 | varchar | 50 |  | √ | ' ' | 问题处理渠道 |
| 20 | fversion | 金蝶云.星空旗舰版版本号 | varchar | 50 |  | √ | ' ' | 金蝶云.星空旗舰版版本号 |
| 21 | fcreateuidname | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 22 | fextend16 | 扩展字段16 | varchar | 255 |  | √ | ' ' | 扩展字段16 |
| 23 | fextend15 | 扩展字段15 | varchar | 255 |  | √ | ' ' | 扩展字段15 |
| 24 | fprocessorname | 下一步处理人 | varchar | 50 |  | √ | ' ' | 下一步处理人 |
| 25 | fisforum | 社区协助（废弃） | bpchar | 1 |  | √ | '0' | 社区协助（废弃） |
| 26 | fextend10 | 扩展字段10 | varchar | 255 |  | √ | ' ' | 扩展字段10 |
| 27 | ftenementnumber | 租户编码 | varchar | 50 |  | √ | ' ' | 租户编码 |
| 28 | flistanswer | 列表答复内容展示字段 | varchar | 2000 |  | √ | ' ' | 列表答复内容展示字段 |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fapplication | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 31 | fcreate | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | faging | 账龄 | int4 | 32 |  | √ | 0 | 账龄 |
| 33 | fenvironment | 环境类型 | varchar | 50 |  | √ | ' ' | 环境类型,枚举: current :当前环境 other :其它环境 |
| 34 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: 1 :一般 2 :紧急 |
| 35 | fisdelete | 是否删除 | bpchar | 1 |  | √ | '0' | 是否删除 |
| 36 | ftenementname | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 37 | fextend5 | 扩展字段5 | varchar | 255 |  | √ | ' ' | 扩展字段5 |
| 38 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: B :待答复 A :已答复 C :已解决 D :已撤销 H :已验证 F :验证未通过 G :已关闭 |
| 39 | fextend4 | 扩展字段4 | varchar | 255 |  | √ | ' ' | 扩展字段4 |
| 40 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fextend7 | 扩展字段7 | varchar | 255 |  | √ | ' ' | 扩展字段7 |
| 42 | fextend6 | 扩展字段6 | varchar | 255 |  | √ | ' ' | 扩展字段6 |
| 43 | fextend1 | 扩展字段1 | varchar | 255 |  | √ | ' ' | 扩展字段1 |
| 44 | fextend3 | 扩展字段3 | varchar | 255 |  | √ | ' ' | 扩展字段3 |
| 45 | fextend2 | 扩展字段2 | varchar | 255 |  | √ | ' ' | 扩展字段2 |
| 46 | fextend9 | 扩展字段9 | varchar | 255 |  | √ | ' ' | 扩展字段9 |
| 47 | fextend8 | 扩展字段8 | varchar | 255 |  | √ | ' ' | 扩展字段8 |
| 48 | fapplicationname | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 49 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: error :错误 need :需求 nature :性能 usability :易用性 else :其他 |

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
