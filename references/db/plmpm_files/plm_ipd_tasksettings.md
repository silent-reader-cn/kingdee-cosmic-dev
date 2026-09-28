# 任务设置-plm_ipd_tasksettings

## 任务设置-多语言表 t_plm_ipd_tasksetting_l

- **表名称：** 任务设置-多语言表
- **表名：** t_plm_ipd_tasksetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_tasksetting_l |  | fpkid |
| 2 | idx_plm_ipd_tasksetting_l_0 |  | fid,flocaleid |

---

## 任务设置-主表 t_plm_ipd_tasksetting

- **表名称：** 任务设置-主表
- **表名：** t_plm_ipd_tasksetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [任务分类 plm_pm_taskkind](../plmpm_files/plm_pm_taskkind.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_tasksetting_m0 |  | fmasterid |
| 2 | pk_plm_ipd_tasksetting |  | fid |
