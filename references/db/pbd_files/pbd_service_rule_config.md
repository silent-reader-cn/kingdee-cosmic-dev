# 业务规则-pbd_service_rule_config

## 插件-子表 t_pbd_service_rule_plugin

- **表名称：** 插件-子表
- **表名：** t_pbd_service_rule_plugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpldescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fplisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 4 | fpldisplayname | 插件名称 | varchar | 255 |  | √ | ' ' | 插件名称 |
| 5 | fplclassname | 插件类名 | varchar | 500 |  | √ | ' ' | 插件类名 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_rule_plugin |  | fentryid |
| 2 | idx_pbd_rule_plugin_fid_fseq |  | fid,fseq |

---

## 插件-子表 t_pbd_service_fieldplugin

- **表名称：** 插件-子表
- **表名：** t_pbd_service_fieldplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpldescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fplisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 4 | fpldisplayname | 插件名称 | varchar | 255 |  | √ | ' ' | 插件名称 |
| 5 | fplclassname | 插件类名 | varchar | 500 |  | √ | ' ' | 插件类名 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_fieldplugin |  | fentryid |
| 2 | idx_pbd_field_plugin_fid_fseq |  | fid,fseq |

---

## 业务规则-主表 t_pbd_service_rule

- **表名称：** 业务规则-主表
- **表名：** t_pbd_service_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | foperator | 业务触发场景 | varchar | 50 |  | √ | ' ' | 业务触发场景 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fruletype | 接口用途 | bpchar | 1 |  | √ | ' ' | 接口用途,枚举: A :校验 B :填充 C :展示 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftriggertype | 触发类别 | bpchar | 1 |  | √ | ' ' | 触发类别,枚举: A :业务操作 B :条件触发 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fplatformapild | 来源接口名称 | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 12 | fbillid | 业务调用方案BillId | int8 | 64 |  | √ | 0 | 业务调用方案BillId |
| 13 | fbillentity | 关联业务单据或组件 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fstandardapild | 标准接口名称 | int8 | 64 |  | √ | 0 | [接口映射方案 pbd_standard_api](../pbd_files/pbd_standard_api.md) |
| 15 | fentryid | 业务调用方案EntryID | int8 | 64 |  | √ | 0 | 业务调用方案EntryID |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_rule |  | fid |
| 2 | idx_pbd_service_rule_fnumber |  | fbillno |

---

## 输出条件-子表 t_pbd_service_rule_fout

- **表名称：** 输出条件-子表
- **表名：** t_pbd_service_rule_fout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutputsourcefield | 来源字段名称 | varchar | 80 |  | √ | ' ' | 来源字段名称 |
| 3 | foutputsourcefielddesc | 来源字段描述 | varchar | 255 |  | √ | ' ' | 来源字段描述 |
| 4 | foutputfieldformuladesc | 计算公式 | varchar | 50 |  | √ | ' ' | 计算公式 |
| 5 | foutputfieldtype | 取值规则 | varchar | 50 |  | √ | ' ' | 取值规则,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 3 :常量 |
| 6 | foutputtargetfield | 目标单字段 | varchar | 80 |  | √ | ' ' | 目标单字段 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutputstargetfieldname | 目标单字段 | varchar | 255 |  | √ | ' ' | 目标单字段 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | foutputfieldformula | 计算公式 | varchar | 50 |  | √ | ' ' | 计算公式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_rule_fout_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_service_rule_fout |  | fentryid |

---

## 输入条件-子表 t_pbd_service_rule_fin

- **表名称：** 输入条件-子表
- **表名：** t_pbd_service_rule_fin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finputtargetfield | 目标单字段 | varchar | 80 |  | √ | ' ' | 目标单字段 |
| 3 | finputtargetfieldname | 目标单字段 | varchar | 255 |  | √ | ' ' | 目标单字段 |
| 4 | finputtargetconstant | 常量 | varchar | 255 |  | √ | ' ' | 常量 |
| 5 | finputsourcefielddesc | 来源字段描述 | varchar | 255 |  | √ | ' ' | 来源字段描述 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | finputsourcefield | 来源字段名称 | varchar | 80 |  | √ | ' ' | 来源字段名称 |
| 9 | finputfieldtype | 匹配方式 | varchar | 50 |  | √ | ' ' | 匹配方式,枚举: = :等于 in :in |
| 10 | finputremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_rule_fin |  | fentryid |
| 2 | idx_pbd_rule_fin_fid_fseq |  | fid,fseq |

---

## 输入条件-子表 t_pbd_service_rule_rin

- **表名称：** 输入条件-子表
- **表名：** t_pbd_service_rule_rin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finputsrcrulefielddesc | 来源字段描述 | varchar | 255 |  | √ | ' ' | 来源字段描述 |
| 3 | finputsrcrulefield | 来源字段名称 | varchar | 80 |  | √ | ' ' | 来源字段名称 |
| 4 | finputtarrulefield | 目标单字段 | varchar | 80 |  | √ | ' ' | 目标单字段 |
| 5 | finputruletype | 匹配方式 | varchar | 50 |  | √ | ' ' | 匹配方式,枚举: = :等于 in :in |
| 6 | finputruleremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finputtarrulefieldname | 目标单字段 | varchar | 255 |  | √ | ' ' | 目标单字段 |
| 9 | finputtarruletconstant | 常量 | varchar | 255 |  | √ | ' ' | 常量 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_rule_rin |  | fentryid |
| 2 | idx_pbdrule_rin_fid_fseq |  | fid,fseq |

---

## 输出条件-子表 t_pbd_service_rule_rout

- **表名称：** 输出条件-子表
- **表名：** t_pbd_service_rule_rout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutputsrcrulefield | 来源字段名称 | varchar | 80 |  | √ | ' ' | 来源字段名称 |
| 3 | foutputtarrulefield | 目标单字段 | varchar | 80 |  | √ | ' ' | 目标单字段 |
| 4 | foutputruleremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | foutputruletype | 匹配方式 | varchar | 50 |  | √ | ' ' | 匹配方式,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 3 :常量 |
| 6 | foutputtarrulefieldname | 目标单字段 | varchar | 255 |  | √ | ' ' | 目标单字段 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutputtarruletconstant | 常量 | varchar | 255 |  | √ | ' ' | 常量 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | foutputsrcrulefielddesc | 来源字段描述 | varchar | 255 |  | √ | ' ' | 来源字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_rule_rout |  | fentryid |
| 2 | idx_pbd_rule_out_fid_fseq |  | fid,fseq |
