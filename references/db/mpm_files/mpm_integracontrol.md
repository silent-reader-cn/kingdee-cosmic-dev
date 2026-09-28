# 集成控制-mpm_integracontrol

## 集成控制-多语言表 t_mpm_intecontrol_l

- **表名称：** 集成控制-多语言表
- **表名：** t_mpm_intecontrol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_intecontrol_fidflid |  | fid,flocaleid |
| 2 | pk_mpm_intecontrol_l |  | fpkid |

---

## 集成控制-主表 t_mpm_intecontrol

- **表名称：** 集成控制-主表
- **表名：** t_mpm_intecontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisfinishautostart | 前置任务完成，后置任务自动启动 | bpchar | 1 |  | √ | '0' | 前置任务完成，后置任务自动启动 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fplanctrlmode | 项目计划控制方向 | bpchar | 1 |  | √ | 'A' | 项目计划控制方向,枚举: A :自下而上 B :自上而下（控制完成日期） C :自上而下（控制开始和完成日期） |
| 8 | fisfirstkeytask | 开口任务标记为关键任务 | bpchar | 1 |  | √ | '0' | 开口任务标记为关键任务 |
| 9 | fistaskmanagerreport | 只允许任务负责人汇报进度 | bpchar | 1 |  | √ | '0' | 只允许任务负责人汇报进度 |
| 10 | fkeypaththreshold | 关键路径阈值 | int8 | 64 |  | √ | 0 | 关键路径阈值 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fplanpublishmode | 项目计划发布方式 | bpchar | 1 |  | √ | 'B' | 项目计划发布方式,枚举: A :项目经理集中发布 B :编制人发布 |
| 15 | fischeckprojectinspect | 项目任务（“已取消”除外）全部已完成才允许项目终验 | bpchar | 1 |  | √ | '0' | 项目任务（“已取消”除外）全部已完成才允许项目终验 |
| 16 | frelcontrolstatus | 按前后任务间的依赖关系控制后置任务状态的执行 | bpchar | 1 |  | √ | 'A' | 按前后任务间的依赖关系控制后置任务状态的执行,枚举: A :不控制 B :提醒 C :严格控制 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 20 | fiscooperative | 启用协同编制 | bpchar | 1 |  | √ | '0' | 启用协同编制 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fuseprostage | 启用项目阶段 | bpchar | 1 |  | √ | '0' | 启用项目阶段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_intecontrol |  | fid |
| 2 | idx_mpm_intecontrol_fnumber |  | fnumber |
