# 风险预警清单-pbd_monitor_result

## 检查结果分录-子表 t_pbd_monitorresentry_res

- **表名称：** 检查结果分录-子表
- **表名：** t_pbd_monitorresentry_res

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcount1 | 数量 | int4 | 32 |  | √ | 0 | 数量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcheckresult1id | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitorresentry_res_id |  | fid |
| 2 | pk_pbd_monitorresentry_res |  | fentryid |

---

## 检查项统计分录-子表 t_pbd_monitorresentry_itm

- **表名称：** 检查项统计分录-子表
- **表名：** t_pbd_monitorresentry_itm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcount2 | 数量 | int4 | 32 |  | √ | 0 | 数量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem2 | 检查项名称 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcheckresult2id | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitorresentry_itm |  | fentryid |
| 2 | idx_pbd_monitorresentry_itm_id |  | fid |

---

## 风险预警清单-主表 t_pbd_monitorresult

- **表名称：** 风险预警清单-主表
- **表名：** t_pbd_monitorresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 生成预警清单时间 | timestamp | 0 |  |  | null | 生成预警清单时间 |
| 8 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmonitorschemeid | 监控方案编码 | int8 | 64 |  | √ | 0 | [风险监控方案 pbd_monitor_scheme](../pbd_files/pbd_monitor_scheme.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftargetno | 监控目标编码 | varchar | 80 |  | √ | ' ' | 监控目标编码 |
| 14 | fkey | 方案编码监控单据id | varchar | 150 |  | √ | ' ' | 方案编码监控单据id |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftargetid | 监控目标主键 | varchar | 50 |  | √ | ' ' | 监控目标主键 |
| 17 | fbillno | 预警编码 | varchar | 80 |  | √ | ' ' | 预警编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitorresult_ftargeti |  | ftargetid |
| 2 | pk_pbd_monitorresult |  | fid |
| 3 | idx_pbd_monitorresult_fbillno |  | fbillno |
| 4 | idx_pbd_monitorresult_fkey |  | fkey |

---

## 指标明细-子表 t_pbd_subindicator

- **表名称：** 指标明细-子表
- **表名：** t_pbd_subindicator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | findicatorid | 指标 | int8 | 64 |  | √ | 0 | [风险指标 pbd_indicator](../pbd_files/pbd_indicator.md) |
| 2 | findicatorresult | 指标结果 | varchar | 2000 |  | √ | ' ' | 指标结果 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | findicatorresult_tag | 指标结果_详情 | text | 0 |  |  | null | 指标结果_详情 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pbd_subindicator_entryid |  | fentryid |
| 2 | pk_pbd_subindicator |  | fdetailid |

---

## 按监控维度统计分录-子表 t_pbd_monitorresentry

- **表名称：** 按监控维度统计分录-子表
- **表名：** t_pbd_monitorresentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimvalueid | 监控维度值id | varchar | 50 |  | √ | ' ' | 监控维度值id |
| 3 | fcheckresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 4 | ffiltercondition_tag | 触发条件_详情 | text | 0 |  |  | null | 触发条件_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fconfirmresultid | 确认结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 7 | fcheckitem | 检查项名称 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 8 | fdimvalue | 监控维度值 | varchar | 255 |  | √ | ' ' | 监控维度值 |
| 9 | freason | 调整说明 | varchar | 512 |  | √ | ' ' | 调整说明 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 触发条件 | varchar | 2000 |  | √ | ' ' | 触发条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitorresentry_fid |  | fid |
| 2 | pk_pbd_monitorresentry |  | fentryid |

---

## 关联检查项-多选基础资料表 t_pbd_monitorlevres_items

- **表名称：** 关联检查项-多选基础资料表
- **表名：** t_pbd_monitorlevres_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitorlevres_items_en |  | fentryid |
| 2 | pk_pbd_monitorlevres_items |  | fpkid |
