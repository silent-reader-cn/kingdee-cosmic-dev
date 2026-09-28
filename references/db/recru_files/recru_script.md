# 执行脚本-recru_script

## 执行脚本-多语言表 t_recru_script_l

- **表名称：** 执行脚本-多语言表
- **表名：** t_recru_script_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 脚本名称 | varchar | 50 |  | √ | ' ' | 脚本名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_script_l_fid |  | fid,flocaleid |
| 2 | pk_recru_script_l |  | fpkid |

---

## 执行脚本-主表 t_recru_script

- **表名称：** 执行脚本-主表
- **表名：** t_recru_script

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 脚本名称 | varchar | 50 |  | √ | ' ' | 脚本名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fscriptnode | 脚本节点 | varchar | 50 |  | √ | ' ' | 脚本节点,枚举: start :开始 append :执行中 end :执行完成 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fscript | 脚本 | varchar | 255 |  | √ | ' ' | 脚本 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :发布jd 2 :搜索简历 |
| 13 | fnodeid | 任务执行节点 | int8 | 64 |  | √ | 0 | [任务节点编排 recru_agenttask](../recru_files/recru_agenttask.md) |
| 14 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fscript_tag | 脚本_详情 | text | 0 |  |  | null | 脚本_详情 |
| 16 | fnumber | 脚本编码 | varchar | 30 |  | √ | ' ' | 脚本编码 |
| 17 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道管理 recru_channel](../recru_files/recru_channel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__recru_script_nodeid |  | fnodeid |
| 2 | pk_recru_script |  | fid |
