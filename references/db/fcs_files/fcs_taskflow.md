# 任务编排-fcs_taskflow

## 任务编排-多语言表 t_fcs_taskflow_l

- **表名称：** 任务编排-多语言表
- **表名：** t_fcs_taskflow_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_taskflow_l |  | fpkid |
| 2 | idx_t_fcs_taskflow_l |  | fid,flocaleid |

---

## 组织单据体-子表 t_fcs_taskflow_org

- **表名称：** 组织单据体-子表
- **表名：** t_fcs_taskflow_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_taskflow_org |  | fentryid |
| 2 | idx_fcs_taskflow_org |  | fid |

---

## 任务编排-主表 t_fcs_taskflow

- **表名称：** 任务编排-主表
- **表名：** t_fcs_taskflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 3 | fbeginoperatename | fbeginoperatename | varchar | 50 |  | √ | ' ' |  |
| 4 | fbizfilterconfig_tag | 适用业务范围参数_详情 | text | 0 |  |  | null | 适用业务范围参数_详情 |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | fbizappid | fbizappid | varchar | 50 |  | √ | ' ' |  |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbizfilterconfig | 适用业务范围参数 | varchar | 255 |  | √ | ' ' | 适用业务范围参数 |
| 9 | fisrevoperate | fisrevoperate | bpchar | 1 |  | √ | '0' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisbackgroundstart | fisbackgroundstart | bpchar | 1 |  | √ | '0' |  |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fqueryderiction | fqueryderiction | varchar | 50 |  | √ | ' ' |  |
| 15 | fexecutorid | fexecutorid | int8 | 64 |  | √ | 0 |  |
| 16 | fexceptionreceiverid | fexceptionreceiverid | int8 | 64 |  | √ | 0 |  |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fbeginoperate | 触发操作 | varchar | 50 |  | √ | ' ' | 触发操作,枚举: |
| 22 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbizentityid | fbizentityid | varchar | 50 |  | √ | ' ' |  |
| 25 | fbizfilter | 适用业务范围 | varchar | 50 |  | √ | ' ' | 适用业务范围 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fisshowdetails | fisshowdetails | bpchar | 1 |  | √ | '0' |  |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_taskflow |  | fenable,fbizentityid,fbeginoperate |
| 2 | pk_t_fcs_taskflow |  | fid |

---

## 任务流单据体-子表 t_fcs_taskflow_task

- **表名称：** 任务流单据体-子表
- **表名：** t_fcs_taskflow_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmserviceconfig_tag | 微服务参数_详情 | text | 0 |  |  | null | 微服务参数_详情 |
| 3 | foperatename | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作 |
| 4 | fisacrossbill | fisacrossbill | bpchar | 1 |  | √ | '0' |  |
| 5 | fmainentityid | fmainentityid | varchar | 50 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmserviceconfig | 微服务参数 | varchar | 255 |  | √ | ' ' | 微服务参数 |
| 8 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 9 | fappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fiscycle | fiscycle | bpchar | 1 |  | √ | '0' |  |
| 11 | foperatekey | 执行操作编码 | varchar | 50 |  | √ | ' ' | 执行操作编码 |
| 12 | fmicroservice | 微服务 | varchar | 50 |  | √ | ' ' | 微服务 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_taskflow_task |  | fentryid |
| 2 | idx_fcs_taskflow_task |  | fid |
