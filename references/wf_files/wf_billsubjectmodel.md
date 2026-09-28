# 单据流程属性-wf_billsubjectmodel

## 单据流程属性-主表 t_wf_billsubjectmodel

- **表名称：** 单据流程属性-主表
- **表名：** t_wf_billsubjectmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbiztraceno | 业务跟踪号 | varchar | 100 |  | √ | ' ' | 业务跟踪号 |
| 3 | fbillsubmobname | MOB单据主题名称 | text | 0 |  |  | null | MOB单据主题名称 |
| 4 | fentitynumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 5 | fformkeyname | PC查看页面名称 | varchar | 255 |  | √ | ' ' | PC查看页面名称 |
| 6 | fviewchatflowpermplugin | 查看流程图权限插件 | text | 0 |  |  | null | 查看流程图权限插件 |
| 7 | fbillsubjectmob | MOB单据主题 | text | 0 |  |  | null | MOB单据主题 |
| 8 | fbillsubjectname | PC单据主题显示名称(废弃) | text | 0 |  |  | null | PC单据主题显示名称(废弃) |
| 9 | fsubjectshowname | PC单据主题显示名称 | varchar | 3000 |  | √ | ' ' | PC单据主题显示名称 |
| 10 | fmainfield | 云之家任务集成关键业务字段 | varchar | 2000 |  | √ | ' ' | 云之家任务集成关键业务字段,枚举: |
| 11 | freferorganization | 参照组织 | varchar | 255 |  | √ | ' ' | 参照组织 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fcreatorid | 创建人id | int8 | 64 |  | √ | 0 | 创建人id |
| 14 | fsample | PC样例 | varchar | 3000 |  |  | ' ' | PC样例 |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmobileformkeyname | 移动端查看页面名称 | varchar | 255 |  | √ | ' ' | 移动端查看页面名称 |
| 17 | fpushstatusplugin | 查看下推状态插件 | text | 0 |  |  | null | 查看下推状态插件 |
| 18 | fmodifierid | 修改人id | int8 | 64 |  | √ | 0 | 修改人id |
| 19 | fformkey | PC查看页面编码 | varchar | 50 |  | √ | ' ' | PC查看页面编码 |
| 20 | fbillsubject | PC单据主题 | text | 0 |  |  | null | PC单据主题 |
| 21 | fbiztracenodesc | 业务跟踪号描述 | varchar | 100 |  | √ | ' ' | 业务跟踪号描述 |
| 22 | fbillname | 单据名称 | varchar | 115 |  | √ | ' ' | 单据名称 |
| 23 | fbusinessfieldmappinginfo | 业务字段映射关系配置 | text | 0 |  |  | null | 业务字段映射关系配置 |
| 24 | fbillid | 单据id | varchar | 36 |  | √ | ' ' | 单据id |
| 25 | fpermissionsplugin | 单据权限插件 | text | 0 |  |  | null | 单据权限插件 |
| 26 | fmobileformkey | 移动端查看页面编码 | varchar | 50 |  | √ | ' ' | 移动端查看页面编码 |
| 27 | ffilterapprovalrecordplg | 审批记录权限插件 | text | 0 |  |  | null | 审批记录权限插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_billsubjectmodel_pkey |  | fid |
| 2 | idx_wf_billsubjectmodel_entity |  | fentitynumber |

---

## 单据流程属性-多语言表 t_wf_billsubjectmodel_l

- **表名称：** 单据流程属性-多语言表
- **表名：** t_wf_billsubjectmodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillsubject | PC单据主题 | text | 0 |  |  | null | PC单据主题 |
| 3 | fbillsubmobname | MOB单据主题名称 | text | 0 |  |  | null | MOB单据主题名称 |
| 4 | fformkeyname | PC查看页面名称 | varchar | 255 |  | √ | ' ' | PC查看页面名称 |
| 5 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 6 | fbillsubjectmob | MOB单据主题 | text | 0 |  |  | null | MOB单据主题 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fbiztracenodesc | 业务跟踪号描述 | varchar | 100 |  | √ | ' ' | 业务跟踪号描述 |
| 9 | fbillname | 单据名称 | varchar | 115 |  | √ | ' ' | 单据名称 |
| 10 | fbillsubjectname | PC单据主题显示名称(废弃) | text | 0 |  |  | null | PC单据主题显示名称(废弃) |
| 11 | fsubjectshowname | PC单据主题显示名称 | varchar | 3000 |  | √ | ' ' | PC单据主题显示名称 |
| 12 | fsample | PC样例 | varchar | 3000 |  |  | ' ' | PC样例 |
| 13 | fmobileformkeyname | 移动端查看页面名称 | varchar | 255 |  | √ | ' ' | 移动端查看页面名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_billsubjectmodel_loc |  | fid,flocaleid |
| 2 | t_wf_billsubjectmodel_l_pkey |  | fpkid |
