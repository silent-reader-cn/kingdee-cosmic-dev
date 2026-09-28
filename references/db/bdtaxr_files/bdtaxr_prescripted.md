# 预置脚本-bdtaxr_prescripted

## 文件列表-子表 t_bdtaxr_prescriptedentry

- **表名称：** 文件列表-子表
- **表名：** t_bdtaxr_prescriptedentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscriptedplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 3 | ffilename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 4 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: sql :SQL excel :Excel plugin :插件 |
| 5 | fexecutetime | 部署耗时 | int8 | 64 |  | √ | 0 | 部署耗时 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdeploystatus | 部署状态 | varchar | 50 |  | √ | ' ' | 部署状态,枚举: 0 :未部署 1 :部署成功 2 :部署中 3 :部署失败 |
| 8 | fbizobjid | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ffilepath | 文件路径 | varchar | 255 |  | √ | ' ' | 文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_prescriptedentry |  | fentryid |
| 2 | idx_bdtaxr_predentry_fk |  | fid |

---

## 预置脚本-主表 t_bdtaxr_prescripted

- **表名称：** 预置脚本-主表
- **表名：** t_bdtaxr_prescripted

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexecutetime | 部署总耗时 | int8 | 64 |  | √ | 0 | 部署总耗时 |
| 7 | fdeploystatus | 部署状态 | varchar | 50 |  | √ | ' ' | 部署状态,枚举: 0 :未部署 1 :部署成功 2 :部署中 3 :部署失败 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fundeploytip | 未成功部署的提示语 | varchar | 2000 |  | √ | ' ' | 未成功部署的提示语 |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdeploycount | 部署次数 | int8 | 64 |  | √ | 0 | 部署次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_pre_app |  | fbizappid |
| 2 | pk_bdtaxr_prescripted |  | fid |

---

## 预置脚本-多语言表 t_bdtaxr_prescripted_l

- **表名称：** 预置脚本-多语言表
- **表名：** t_bdtaxr_prescripted_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | funexecutetip | funexecutetip | varchar | 2000 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fundeploytip | 未成功部署的提示语 | varchar | 2000 |  | √ | ' ' | 未成功部署的提示语 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_prescripted_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_prescripted_l |  | fpkid |
