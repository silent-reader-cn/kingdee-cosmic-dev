# 数据校验-pds_validatorconfig

## 寻源流程-多选基础资料表 t_pds_validatorsourceflow

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_pds_validatorsourceflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_validatorsourceflow |  | fpkid |
| 2 | idx_pds_validatorflow_fid |  | fid |
| 3 | idx_pds_validatorflow_bid |  | fbasedataid |

---

## 数据校验-主表 t_pds_validatorconfig

- **表名称：** 数据校验-主表
- **表名：** t_pds_validatorconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 校验结果说明 | varchar | 510 |  | √ | ' ' | 校验结果说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | forder | 在同一业务对象+操作类型中的校验顺序 | int4 | 32 |  | √ | 0 | 在同一业务对象+操作类型中的校验顺序 |
| 12 | fisforbidden | 是否允许禁用 | bpchar | 1 |  | √ | '0' | 是否允许禁用 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | foperation | 操作类型 | varchar | 30 |  | √ | ' ' | 操作类型,枚举: save :保存 submit :提交 unsubmit :撤销 audit :审核 unaudit :反审核 allopen :全部开标 tecopen :开技术标 bizopen :开商务标 confirm :确认 reject :打回 push :下推 nextnode :下一步 viehall :竞价大厅 send :发送消息 negopen :议价开标 resend :重新发送 pushscore :下达评分任务 recalculate :重新下达/计算 aptopen :资审开标 pushaptitude :下达资审任务 gather :收集 archive :归档 refuse :拒绝 calculate :综合计算 unenroll :撤回报名 pushevaluate :下达考评任务 autorecommend :自动推荐入围 aptpush :下达资审任务 aptpush2 :下达后审任务 bidpush :下达评标任务 matchcontract :匹配合同 repushaptitude :重新下达资审任务 unpushevaluate :撤销考评任务下达 publish :发布 unpublish :撤销发布 |
| 16 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fpluginname | 数据校验插件 | varchar | 100 |  | √ | ' ' | 数据校验插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_validatorconfig_numer |  | fnumber |
| 2 | idx_pds_validatorconfig_biz |  | fbizobject |
| 3 | pk_pds_validatorconfig |  | fid |
| 4 | idx_pds_validatorconfig_foid |  | foperation |
| 5 | idx_pds_validatorconfig_master |  | fmasterid |

---

## 变更类型-多选基础资料表 t_pds_validatorchgtype

- **表名称：** 变更类型-多选基础资料表
- **表名：** t_pds_validatorchgtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_validatorchgtype_bid |  | fbasedataid |
| 2 | pk_pds_validatorchgtype |  | fpkid |
| 3 | idx_pds_validatorchgtype_fid |  | fid |

---

## 数据校验-多语言表 t_pds_validatorconfig_l

- **表名称：** 数据校验-多语言表
- **表名：** t_pds_validatorconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 校验结果说明 | varchar | 510 |  | √ | ' ' | 校验结果说明 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_validatorconfig_fid |  | fid,flocaleid |
| 2 | pk_pds_validatorconfig_l |  | fpkid |

---

## 寻源方式-多选基础资料表 t_pds_validatorsourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_pds_validatorsourcetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_validatortype_bid |  | fbasedataid |
| 2 | pk_pds_validatorsourcetype |  | fpkid |
| 3 | idx_pds_validatortype_fid |  | fid |

---

## 排除的变更类型-多选基础资料表 t_pds_validatorchgtype2

- **表名称：** 排除的变更类型-多选基础资料表
- **表名：** t_pds_validatorchgtype2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_validatorchgtype2_fid |  | fid |
| 2 | pk_pds_validatorchgtype2 |  | fpkid |
| 3 | idx_pds_validatorchgtype2_bid |  | fbasedataid |

---

## 参数分录-子表 t_pds_validatorparams

- **表名称：** 参数分录-子表
- **表名：** t_pds_validatorparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 4 | fparamname | fparamname | varchar | 50 |  | √ | ' ' |  |
| 5 | fbasedatainfo | 参数说明 | varchar | 512 |  | √ | ' ' | 参数说明 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fismust | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 8 | fparamtype | fparamtype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_validatorparams |  | fentryid |
| 2 | idx_pds_validatorparams_fid |  | fid |

---

## 排除的寻源方式-多选基础资料表 t_pds_validatorsrctype

- **表名称：** 排除的寻源方式-多选基础资料表
- **表名：** t_pds_validatorsrctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_validatorsrctype |  | fpkid |
| 2 | idx_pds_validatorsrctype_fid |  | fid |
| 3 | idx_pds_validatorsrctype_bid |  | fbasedataid |

---

## 排除的寻源流程-多选基础资料表 t_pds_validatorsrcflow

- **表名称：** 排除的寻源流程-多选基础资料表
- **表名：** t_pds_validatorsrcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_validatorsrcflow |  | fpkid |
| 2 | idx_pds_validatorsrcflow_bid |  | fbasedataid |
| 3 | idx_pds_validatorsrcflow_fid |  | fid |
