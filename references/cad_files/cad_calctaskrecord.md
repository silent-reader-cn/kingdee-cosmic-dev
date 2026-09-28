# 卷算报告-cad_calctaskrecord

## 卷算报告-主表 t_cad_calctaskrecord

- **表名称：** 卷算报告-主表
- **表名：** t_cad_calctaskrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 3 | fremark | fremark | int8 | 64 |  | √ | 0 |  |
| 4 | fname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 5 | ftotalsteps | 总步数 | int8 | 64 |  | √ | 0 | 总步数 |
| 6 | fmainorg | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fprogress | 进度(%) | int8 | 64 |  | √ | 0 | 进度(%) |
| 8 | fstarttime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 9 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :执行中 2 :失败 3 :成功 4 :警告 |
| 10 | fnextpagepara | 页面携带参数 | varchar | 1000 |  | √ | ' ' | 页面携带参数 |
| 11 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 13 | fcacheid | 数据缓存ID | varchar | 60 |  | √ | ' ' | 数据缓存ID |
| 14 | ffinishedsteps | 已完成步骤 | int8 | 64 |  | √ | 0 | 已完成步骤 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calctaskrecord_pkey |  | fid |

---

## 卷算报告-多语言表 t_cad_calctaskrecord_l

- **表名称：** 卷算报告-多语言表
- **表名：** t_cad_calctaskrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calctaskrecord_l_pkey |  | fpkid |
| 2 | index_cad_calctaskrecord_l |  | fid,flocaleid |
