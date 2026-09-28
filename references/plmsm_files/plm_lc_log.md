# 物料生命周期转换记录-plm_lc_log

## 物料生命周期转换记录-多语言表 t_plmsm_lc_log_l

- **表名称：** 物料生命周期转换记录-多语言表
- **表名：** t_plmsm_lc_log_l

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
| 1 | pk_plmsm_lc_log_l |  | fpkid |
| 2 | idx_plmsm_lc_log_l_0 |  | fid,flocaleid |

---

## 物料生命周期转换记录-主表 t_plmsm_lc_log

- **表名称：** 物料生命周期转换记录-主表
- **表名：** t_plmsm_lc_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftostatusid | 目标状态id | int8 | 64 |  | √ | 0 | 目标状态id |
| 5 | ftemplateid | 生命周期模板id | int8 | 64 |  | √ | 0 | 生命周期模板id |
| 6 | fmodeltype | 模型标识 | varchar | 100 |  | √ | ' ' | 模型标识 |
| 7 | fworkflowid | 流程id | int8 | 64 |  | √ | 0 | 流程id |
| 8 | flogstatus | 转换日志状态 | varchar | 50 |  | √ | ' ' | 转换日志状态,枚举: 0 :暂存 1 :成功 2 :失败 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodelid | 模型id | int8 | 64 |  | √ | 0 | 模型id |
| 11 | ffromstageld | 源阶段id | int8 | 64 |  | √ | 0 | 源阶段id |
| 12 | fbatchtransferno | 批次号 | int8 | 64 |  | √ | 0 | 批次号 |
| 13 | fitemid | 物料id | int8 | 64 |  | √ | 0 | 物料id |
| 14 | fitemversion | 物料版本号 | varchar | 50 |  | √ | ' ' | 物料版本号 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | ffromstatusid | 源状态id | int8 | 64 |  | √ | 0 | 源状态id |
| 20 | ftostageid | 目标阶段id | int8 | 64 |  | √ | 0 | 目标阶段id |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fdirection | 流转方向 | varchar | 50 |  | √ | ' ' | 流转方向,枚举: 1 :转换 2 :回退 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | flogtype | 转换类型 | varchar | 50 |  | √ | ' ' | 转换类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmsm_lc_log |  | fmodelid,fitemid |
| 2 | pk_plmsm_lc_log |  | fid |
