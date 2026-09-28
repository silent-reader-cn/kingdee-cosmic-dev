# 智能体_业务查数配置-cbi_agent_bizdata

## 兜底配置-子表 t_cbi_agent_biz_fallback

- **表名称：** 兜底配置-子表
- **表名：** t_cbi_agent_biz_fallback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 3 | fquestiontype | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型,枚举: notExistMeasure :查在途指标（查数超范围） persona :人设 simpleChat :闲聊 |
| 4 | ffixedfallback | 固定回复文案/Prompt配置 | varchar | 500 |  | √ | ' ' | 固定回复文案/Prompt配置 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffallbacktype | 回复方式 | varchar | 50 |  | √ | ' ' | 回复方式,枚举: modelProcessing :模型处理 fixedReply :固定回复 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fqueryfield | 查询词 | varchar | 255 |  | √ | ' ' | 查询词 |
| 10 | ffallbackalias | 口语化别名 | varchar | 500 |  | √ | ' ' | 口语化别名 |
| 11 | ffallbackstatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_ag_biz_fallback_fid |  | fid |
| 2 | pk_cbi_agent_biz_fallback |  | fentryid |

---

## 指标维度查数配置-子表 t_cbi_agent_biz_namecf

- **表名称：** 指标维度查数配置-子表
- **表名：** t_cbi_agent_biz_namecf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdragconfig | 1拖N配置id | varchar | 1000 |  | √ | ' ' | 1拖N配置id |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 4 | findexalias | 口语化别名 | varchar | 500 |  | √ | ' ' | 口语化别名 |
| 5 | findexfieldid | 查询词主键id | int8 | 64 |  | √ | 0 | 查询词主键id |
| 6 | findextype | 查数类型 | varchar | 50 |  | √ | ' ' | 查数类型,枚举: dimension :查维度 measure :查指标 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | findexfield | 查询词 | varchar | 255 |  | √ | ' ' | 查询词 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdragconfigdisplay | 1拖N配置 | varchar | 2000 |  | √ | ' ' | 1拖N配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_biz_namecf |  | fentryid |
| 2 | idx_cbi_ag_biz_namecf_fid |  | fid |

---

## 智能体_业务查数配置-主表 t_cbi_agent_bizdata

- **表名称：** 智能体_业务查数配置-主表
- **表名：** t_cbi_agent_bizdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 向量状态 | bpchar | 1 |  | √ | ' ' | 向量状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdatamodelid | 数据源id | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fagentbaseid | 智能体主键id | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 8 | fdefaultquery | 默认查询条件 | varchar | 50 |  | √ | ' ' | 默认查询条件,枚举: today :本日 yesterday :昨日 thisMonth :本月 lastMonth :上月 thisYear :本年 lastYear :去年 userClarify :用户澄清 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_bizdata |  | fid |
| 2 | idx_cbi_ag_biz_agid |  | fagentbaseid |
| 3 | idx_cbi_ag_biz_modelid |  | fdatamodelid |

---

## 业务查数配置-子表 t_cbi_agent_biz_packagecf

- **表名称：** 业务查数配置-子表
- **表名：** t_cbi_agent_biz_packagecf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpackagename | 查询词 | varchar | 255 |  | √ | ' ' | 查询词 |
| 5 | fpackagegroup | 业务查询1拖N配置 | varchar | 1000 |  | √ | ' ' | 业务查询1拖N配置,枚举: |
| 6 | fpackagealias | 口语化别名 | varchar | 500 |  | √ | ' ' | 口语化别名 |
| 7 | fpackagestatus | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpackagetype | 查数类型 | varchar | 50 |  | √ | ' ' | 查数类型,枚举: measureGroup :业务查询 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_ag_biz_packagecf_fid |  | fid |
| 2 | pk_cbi_agent_biz_packagecf |  | fentryid |

---

## 口语化过滤条件配置-子表 t_cbi_agent_biz_filtercf

- **表名称：** 口语化过滤条件配置-子表
- **表名：** t_cbi_agent_biz_filtercf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltername | 过滤词 | varchar | 255 |  | √ | ' ' | 过滤词 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 4 | ffilterstatus | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态 |
| 5 | ffiltertype | 过滤类型 | varchar | 50 |  | √ | ' ' | 过滤类型,枚举: measure :指标 dimensionValue :维度值 |
| 6 | ffilteralias | 口语化别名 | varchar | 500 |  | √ | ' ' | 口语化别名 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | faliascondition | 过滤条件 | varchar | 500 |  | √ | ' ' | 过滤条件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_biz_filtercf |  | fentryid |
| 2 | idx_cbi_ag_biz_filtercf_fid |  | fid |
