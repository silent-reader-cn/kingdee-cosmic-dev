# 接收人（项目角色）配置-plm_pm_mwarning_sender

## 接收人（项目角色）配置-主表 t_plm_pm_mwarning_sender

- **表名称：** 接收人（项目角色）配置-主表
- **表名：** t_plm_pm_mwarning_sender

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwarnschedule | 预警监控方案 | varchar | 50 |  | √ | ' ' | 预警监控方案 |
| 3 | ftype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型,枚举: massage :消息 warning :预警 |
| 4 | fsubscriptionld | 事件订阅 | int8 | 64 |  | √ | 0 | [事件订阅 evt_subscription](../bec_files/evt_subscription.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_mwarning_sender_m0 |  | fwarnschedule |
| 2 | pk_plm_pm_mwarning_sender |  | fid |

---

## 项目角色-多选基础资料表 t_plm_sen_prjroletemplate

- **表名称：** 项目角色-多选基础资料表
- **表名：** t_plm_sen_prjroletemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目权限模板 plm_pm_prjrole](../plmpm_files/plm_pm_prjrole.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_sen_prjroletemplate |  | fpkid |
| 2 | idx_plm_sen_prjroletemplate_fk |  | fid |
