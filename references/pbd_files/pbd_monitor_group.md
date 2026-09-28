# 监控维度分组-pbd_monitor_group

## 监控维度分组-主表 t_pbd_monitor_group

- **表名称：** 监控维度分组-主表
- **表名：** t_pbd_monitor_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fopttype | 操作类型 | bpchar | 1 |  | √ | '1' | 操作类型,枚举: 0 :新增分组 1 :修改分组 2 :删除分组 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fgroupidstr | 第三方分组id | varchar | 50 |  | √ | ' ' | 第三方分组id |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmonitortype | fmonitortype | bpchar | 1 |  | √ | '0' |  |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fapiids | 监控维度ids | varchar | 512 |  | √ | ' ' | 监控维度ids |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitor_group |  | fid |
| 2 | idx_pbd_monitorgroup_fbillno |  | fnumber |

---

## 监控维度分组-多语言表 t_pbd_monitor_group_l

- **表名称：** 监控维度分组-多语言表
- **表名：** t_pbd_monitor_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitor_group_l |  | fpkid |
| 2 | idx_pbd_monitor_group_l_fid |  | fid,flocaleid |

---

## 企业列表-子表 t_pbd_monitor_groupentry

- **表名称：** 企业列表-子表
- **表名：** t_pbd_monitor_groupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextsysapiid | 监控接口 | int8 | 64 |  | √ | 0 | 外部系统API pbd_extsys_api |
| 3 | fapiid | 维度id | varchar | 50 |  | √ | ' ' | 维度id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_mgroup_entry_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_monitor_groupentry |  | fentryid |
