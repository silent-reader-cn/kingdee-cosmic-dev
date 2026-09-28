# 配置-权限包配置-priviitems_instance_conf

## 配置-权限包配置-主表 t_priviitemsinst_conf

- **表名称：** 配置-权限包配置-主表
- **表名：** t_priviitemsinst_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftextfield1 | 权限包描述 | varchar | 50 |  | √ | ' ' | 权限包描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftextfield | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpriviitems_type | 权限包类型 | int8 | 64 |  | √ | 0 | 权限包设置 privilege_items_conf |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprj_number | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_priviitemsinst_conf_m0 |  | fbillno |
| 2 | pk_priviitemsinst_conf |  | fid |

---

## 单据体-子表 t_privilegeinst_entrys

- **表名称：** 单据体-子表
- **表名：** t_privilegeinst_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftextfield2 | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | ftextareafield | 权限项集 | varchar | 1024 |  | √ | ' ' | 权限项集 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privilegeinst_entrys |  | fentryid |
| 2 | idx_privilegeinst_entrys_fk |  | fid |
