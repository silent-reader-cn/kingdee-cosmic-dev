# 日常宣贯单(废弃)-sfc_dailypublicize

## 参会人员-子表 t_sfc_dpub_persentry

- **表名称：** 参会人员-子表
- **表名：** t_sfc_dpub_persentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisjoin | 是否参会 | bpchar | 1 |  | √ | '0' | 是否参会 |
| 3 | fjointime | 参会时间 | timestamp | 0 |  |  | null | 参会时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fperid | 工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fisnewjoin | 是否现场参会新增人员 | bpchar | 1 |  | √ | '0' | 是否现场参会新增人员 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_dpub_persentry |  | fid,fseq |
| 2 | pk_t_sfc_dpub_persentry |  | fentryid |

---

## 会议内容-子表 t_sfc_dpub_mcentry

- **表名称：** 会议内容-子表
- **表名：** t_sfc_dpub_mcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpk | PK | int8 | 64 |  | √ | 0 | PK |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmmcid | 会议模块配置 | int8 | 64 |  | √ | 0 | 会议模块配置(废弃) sfc_meetmodconfig |
| 5 | fcontent | 内容 | varchar | 2000 |  | √ | ' ' | 内容 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fischecked |  | bpchar | 1 |  | √ | '0' |  |
| 8 | fmmcentryid | 会议模块配置分录ID | int8 | 64 |  | √ | 0 | 会议模块配置分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_dpub_mcentry |  | fentryid |
| 2 | idx_t_sfc_dpub_mcentry |  | fid,fseq |

---

## 日常宣贯单(废弃)-主表 t_sfc_dpub

- **表名称：** 日常宣贯单(废弃)-主表
- **表名：** t_sfc_dpub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmeetingbegintime | 会议开始时间 | timestamp | 0 |  |  | null | 会议开始时间 |
| 3 | fmeetingstatus | 会议状态 | varchar | 50 |  | √ | ' ' | 会议状态,枚举: A :未结束 B :已结束 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmcentrytabs_tag | 会议内容页签_详情 | text | 0 |  |  | null | 会议内容页签_详情 |
| 6 | fmeetingduration | 会议时长 | varchar | 50 |  | √ | ' ' | 会议时长 |
| 7 | fpers | 参会人员 | varchar | 255 |  | √ | ' ' | 参会人员 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpers_tag | 参会人员_详情 | text | 0 |  |  | ' ' | 参会人员_详情 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmeetingendtime | 会议结束时间 | timestamp | 0 |  |  | null | 会议结束时间 |
| 12 | fmocentrytabs | 会议相关内容页签 | varchar | 255 |  | √ | ' ' | 会议相关内容页签 |
| 13 | fmrtypeid | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 14 | foriginatorid | 会议发起人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | foriginatororgid | 会议发起部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fmeetingtypeid | 会议类型 | int8 | 64 |  | √ | 0 | 会议类型(废弃) sfc_meettype |
| 23 | fmeetingloc | 会议地点 | varchar | 255 |  | √ | ' ' | 会议地点 |
| 24 | fovhldeviceid | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 25 | findustryid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 26 | fmocentrytabs_tag | 会议相关内容页签_详情 | text | 0 |  |  | null | 会议相关内容页签_详情 |
| 27 | fistemplate | 是否为模板 | bpchar | 1 |  | √ | '0' | 是否为模板 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fmcentrytabs | 会议内容页签 | varchar | 255 |  | √ | ' ' | 会议内容页签 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_dpub |  | fid |
| 2 | idx_t_sfc_dpub |  | fbillno,fcreatorid |

---

## 会议相关内容-子表 t_sfc_dpub_mocentry

- **表名称：** 会议相关内容-子表
- **表名：** t_sfc_dpub_mocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpk | PK | int8 | 64 |  | √ | 0 | PK |
| 3 | fotherdesc | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmmcid | 会议模块配置 | int8 | 64 |  | √ | 0 | 会议模块配置(废弃) sfc_meetmodconfig |
| 6 | fcontent | 内容 | varchar | 2000 |  | √ | ' ' | 内容 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fischecked |  | bpchar | 1 |  | √ | '0' |  |
| 9 | fmmcentryid | 会议模块配置分录ID | int8 | 64 |  | √ | 0 | 会议模块配置分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_dpub_mocentry |  | fentryid |
| 2 | idx_t_sfc_dpub_mocentry |  | fid,fseq |
